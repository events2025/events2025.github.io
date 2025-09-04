import pandas as pd
import re
import yaml

# --- Config kept minimal (paths are fixed) ---
MASTER_CSV_PATH = 'data/Add Item to "Events in Context" Knowledge Base_1.csv'

# Which markdown gets which Type (normalized). Same structure as your original mapping.
files_to_process = [
    ('websites.md',  'website'),
    ('datasets.md',  'dataset'),
    ('tools.md',     'tool'),
    ('tutorials.md', 'tutorial'),
    ('methods.md',   'paper or method'),          # Papers & Methods
    ('conferences.md','conference or journal'),   # Conferences + Journals
]

# --- Helpers (same shape as your code) ---
def clean_title(title: str) -> str:
    title = re.sub(r'[^\w\s-]', '', str(title))
    return title.replace(' ', '_').lower()

def substitute_placeholders(text: str, row: pd.Series) -> str:
    placeholders = re.findall(r'\(\((.*?)\)\)', text)
    out = text
    for placeholder in placeholders:
        key = placeholder.strip()
        value = str(row.get(key, ''))
        value = value.replace('\\', '\\\\').replace('$', '\\$')
        out = out.replace(f'(({placeholder}))', value)
    return out

def ensure_image_thumb(row: pd.Series) -> str:
    """
    Minimal: do NOT create/copy anything.
    If Image already points to assets/images/thumb, keep it (normalize leading slash).
    Else, point to /assets/images/thumb/<cleaned title>.jpg
    """
    img = str(row.get('Image', '')).strip()
    if 'assets/images/thumb' in img:
        return img if img.startswith('/') else '/' + img
    cleaned = clean_title(row.get('Title', 'item'))
    return f'/assets/images/thumb/{cleaned}.jpg'

def _parse_year(y):
    try:
        return int(str(y)[:4])
    except Exception:
        return None

def _standardize_subsection(x):
    s = str(x).strip().lower()
    if 'conference' in s or s == 'conf' or s == 'conferences':
        return 'conference'
    if 'journal' in s or s == 'journals':
        return 'journal'
    return s if s in ('conference', 'journal') else 'journal'  # default

def _normalize_type(s: str) -> str:
    """
    Strip emoji/punct, lowercase, and bucket to match files_to_process types.
    """
    if s is None:
        return ''
    t = re.sub(r'[^\w\s-]', ' ', str(s)).lower()
    t = re.sub(r'\s+', ' ', t).strip()
    if 'website' in t: return 'website'
    if 'dataset' in t: return 'dataset'
    if 'tool' in t: return 'tool'
    if 'tutorial' in t: return 'tutorial'
    if 'paper' in t or 'method' in t: return 'paper or method'
    if 'conference' in t or 'journal' in t: return 'conference or journal'
    return t

def _simplify_for_filename(text: str, max_len: int = 30) -> str:
    if text is None:
        return 'unknown'
    t = str(text).strip().lower()
    t = re.sub(r'[^\w\s\-_]', '', t)
    t = re.sub(r'\s+', '-', t).strip('-_')
    return (t[:max_len] or 'unknown')

# --- Load the single master CSV ---
try:
    df_master = pd.read_csv(MASTER_CSV_PATH, encoding='utf-8')
except FileNotFoundError:
    raise SystemExit(f"CSV not found: {MASTER_CSV_PATH}")
except pd.errors.EmptyDataError:
    raise SystemExit(f"CSV is empty: {MASTER_CSV_PATH}")
except Exception as e:
    raise SystemExit(f"Error reading {MASTER_CSV_PATH}: {e}")

# Ensure expected columns exist (like your original)
for c in ('Image','Title','URL','Description'):
    if c not in df_master.columns:
        df_master[c] = ''

# Normalize images and Type
df_master['Image'] = df_master.apply(ensure_image_thumb, axis=1)
df_master['_NormType'] = df_master['Type'].apply(_normalize_type)

# --- Render each markdown page from the master CSV, filtering by Type ---
for markdown_filename, want_type in files_to_process:
    print(f"\n==> Building {markdown_filename} from master CSV (type == {want_type})")

    df = df_master[df_master['_NormType'] == want_type].copy()

    # Load template
    template_path = f'docs/{markdown_filename}.template'
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            md = f.read()
    except FileNotFoundError:
        print(f"Template not found: {template_path}. Skipping {markdown_filename}.")
        continue

    start_c = '<!-- START -->'
    stop_c = '<!-- STOP -->'
    i1 = md.find(start_c)
    i2 = md.find(stop_c, i1)
    if i1 == -1 or i2 == -1:
        print(f"No START/STOP markers in {markdown_filename}. Skipping.")
        continue
    block = md[i1+len(start_c):i2].strip()

    generated = ''

    # Per-page grouping logic (unchanged from your code)
    if markdown_filename == 'datasets.md':
        if 'Subsection' not in df.columns:
            print("Warning: No 'Subsection' in master CSV; defaulting to 'Contexts (Environment & Climate)'.")
            df['Subsection'] = 'Contexts (Environment & Climate)'
        sections_to_show = [
            'Contexts (Environment & Climate)',
            'Contexts (Misc Data & APIs)',
            'Contexts (Population Data & Mobility)',
            'Events',
        ]
        for section in sections_to_show:
            sub_df = df[df['Subsection'] == section].copy()
            if not sub_df.empty:
                sub_df = sub_df.sort_values(['Title']).reset_index(drop=True)
                generated += f"\n\n<p class=\"dataset-subsection\">{section}</p>\n\n"
                for _, row in sub_df.iterrows():
                    generated += substitute_placeholders(block, row) + "\n\n"

    elif markdown_filename == 'methods.md':
        if 'Year' not in df.columns:
            df['Year'] = ''
        df['_YearInt'] = df['Year'].apply(_parse_year)
        df = df.sort_values(by=['_YearInt', 'Title'], ascending=[True, True])
        years = [y for y in df['_YearInt'].dropna().unique()]
        for y in years:
            sub_df = df[df['_YearInt'] == y].copy()
            if not sub_df.empty:
                generated += f"\n\n<p class=\"paper-year\">{int(y)}</p>\n\n"
                for _, row in sub_df.iterrows():
                    generated += substitute_placeholders(block, row) + "\n\n"
        unk_df = df[df['_YearInt'].isna()].copy()
        if not unk_df.empty:
            generated += "\n\n<p class=\"paper-year\">Unknown Year</p>\n\n"
            unk_df = unk_df.sort_values(['Title']).reset_index(drop=True)
            for _, row in unk_df.iterrows():
                generated += substitute_placeholders(block, row) + "\n\n"

    elif markdown_filename == 'conferences.md':
        if 'Subsection' not in df.columns:
            df['Subsection'] = 'journal'
        df['Subsection'] = df['Subsection'].apply(_standardize_subsection)
        order = ['conference', 'journal']
        labels = {'conference': 'Conferences', 'journal': 'Journals'}
        for sec in order:
            sub_df = df[df['Subsection'] == sec].copy()
            if not sub_df.empty:
                sub_df = sub_df.sort_values(['Title']).reset_index(drop=True)
                generated += f"\n\n<p class=\"venue-subsection\">{labels[sec]}</p>\n\n"
                for _, row in sub_df.iterrows():
                    generated += substitute_placeholders(block, row) + "\n\n"
    else:
        # Default: simple stream in Title order
        df = df.sort_values(['Title']).reset_index(drop=True)
        for _, row in df.iterrows():
            generated += substitute_placeholders(block, row) + "\n\n"

    # Write out
    new_block = f"{start_c}\n{generated.strip()}\n{stop_c}"
    md = md[:i1] + new_block + md[i2+len(stop_c):]
    out_path = f'docs/{markdown_filename}'
    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Updated {out_path}")
    except Exception as e:
        print(f"Error writing {out_path}: {e}")

print("\nAll pages processed from master CSV.")

# --- YAML: one file per row under data/Yaml_files/ ---
print("\n==> Writing per-row YAML files")
CANON = ["Timestamp","Type","Title","URL","Description","Contributor Id","Image","Subsection"]
for _, row in df_master.iterrows():
    type_part  = _simplify_for_filename(row.get("Type", "unknown"),  max_len=30)
    title_part = _simplify_for_filename(row.get("Title", "unknown"), max_len=30)
    yaml_path = f"data/Yaml_files/{type_part}_{title_part}.yaml"
    data = {k: row.get(k, "") for k in CANON}
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

print("YAML rows written to data/Yaml_files/")
