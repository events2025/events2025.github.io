import re, glob, yaml, pandas as pd

# Which markdown page consumes which normalized Type
files_to_process = [
    ('websites.md',  'website'),
    ('datasets.md',  'dataset'),
    ('tools.md',     'tool'),
    ('tutorials.md', 'tutorial'),
    ('methods.md',   'paper or method'),
    ('conferences.md','conference or journal'),
]

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

def _parse_year(y):
    try: return int(str(y)[:4])
    except Exception: return None

def _standardize_subsection(x):
    s = str(x).strip().lower()
    if 'conference' in s or s in ('conf','conferences'): return 'conference'
    if 'journal' in s or s == 'journals': return 'journal'
    return s if s in ('conference','journal') else 'journal'

def _normalize_type(s: str) -> str:
    if s is None: return ''
    t = re.sub(r'[^\w\s-]', ' ', str(s)).lower()
    t = re.sub(r'\s+', ' ', t).strip()
    if 'website' in t: return 'website'
    if 'dataset' in t: return 'dataset'
    if 'tool' in t: return 'tool'
    if 'tutorial' in t: return 'tutorial'
    if 'paper' in t or 'method' in t: return 'paper or method'
    if 'conference' in t or 'journal' in t: return 'conference or journal'
    return t

# --- Load all YAML rows ---
rows = []
for path in sorted(glob.glob('data/Yaml_files/*.yaml')):
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f) or {}
        rows.append(data)

if not rows:
    raise SystemExit("No YAML files found under data/Yaml_files/")

df_master = pd.DataFrame(rows)

# Ensure expected columns exist
for c in ('Image','Title','URL','Description','Subsection','Type','Year'):
    if c not in df_master.columns:
        df_master[c] = ''

# Normalize type
df_master['_NormType'] = df_master['Type'].apply(_normalize_type)

# --- Render each markdown page from YAML, filtering by type ---
for markdown_filename, want_type in files_to_process:
    print(f"\n==> Building {markdown_filename} from YAML (type == {want_type})")
    df = df_master[df_master['_NormType'] == want_type].copy()

    # Load template
    template_path = f'docs/{markdown_filename}.template'
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            md = f.read()
    except FileNotFoundError:
        print(f"Template not found: {template_path}. Skipping {markdown_filename}.")
        continue

    start_c, stop_c = '<!-- START -->', '<!-- STOP -->'
    i1, i2 = md.find(start_c), md.find(stop_c, md.find(start_c))
    if i1 == -1 or i2 == -1:
        print(f"No START/STOP markers in {markdown_filename}. Skipping.")
        continue
    block = md[i1+len(start_c):i2].strip()

    generated = ''

    if markdown_filename == 'datasets.md':
        if 'Subsection' not in df.columns: df['Subsection'] = 'Contexts (Environment & Climate)'
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
        df = df.sort_values(['Title']).reset_index(drop=True)
        for _, row in df.iterrows():
            generated += substitute_placeholders(block, row) + "\n\n"

    elif markdown_filename == 'conferences.md':
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
        df = df.sort_values(['Title']).reset_index(drop=True)
        for _, row in df.iterrows():
            generated += substitute_placeholders(block, row) + "\n\n"

    # Write page
    new_block = f"{start_c}\n{generated.strip()}\n{stop_c}"
    md = md[:i1] + new_block + md[i2+len(stop_c):]
    out_path = f'docs/{markdown_filename}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md)

print("\nAll pages processed from YAML.")
