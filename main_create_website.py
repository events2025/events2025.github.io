import pandas as pd
import re
import os
import shutil

# Which markdown gets which CSV
files_to_process = [
    ('websites.md', 'data/websites.csv'),
    ('datasets.md', 'data/datasets.csv'),
    ('tools.md', 'data/tools.csv'),
    ('tutorials.md', 'data/tutorials.csv'),
    ('methods.md', 'data/papers_methods.csv'),  # Papers & Methods
    ('conferences.md', 'data/venues_conferences_journals.csv'),  # single combined file
]

# Helpers
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
    """Ensure Image points to /assets/images/thumb/<cleaned>.jpg, copying a default if missing."""
    os.makedirs('assets/images/thumb', exist_ok=True)
    img = str(row.get('Image', '')).strip()
    if 'assets/images/thumb' in img:
        return img if img.startswith('/') else '/' + img
    title = row.get('Title', 'item')
    cleaned = clean_title(title)
    new_rel = f'assets/images/thumb/{cleaned}.jpg'
    src = 'assets/images/logo.jpg'   # default placeholder image
    if not os.path.exists(new_rel):
        try:
            shutil.copy(src, new_rel)
        except Exception as e:
            print(f"Error copying default image for '{title}': {e}")
    return '/' + new_rel

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

# Render each markdown from its CSV 
for markdown_filename, csv_path in files_to_process:
    print(f"\n==> Building {markdown_filename} from {csv_path}")

    # Read CSV
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
    except FileNotFoundError:
        print(f"CSV not found: {csv_path}. Skipping {markdown_filename}.")
        continue
    except pd.errors.EmptyDataError:
        print(f"CSV is empty: {csv_path}. Skipping {markdown_filename}.")
        continue
    except Exception as e:
        print(f"Error reading {csv_path}: {e}. Skipping {markdown_filename}.")
        continue

    # Ensure columns exist
    if 'Image' not in df.columns:
        df['Image'] = ''
    if 'Title' not in df.columns:
        df['Title'] = ''
    if 'URL' not in df.columns:
        df['URL'] = ''
    if 'Description' not in df.columns:
        df['Description'] = ''

    # Populate/normalize images
    df['Image'] = df.apply(ensure_image_thumb, axis=1)

    # Load template
    template_path = f'docs/{markdown_filename}.template'
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            md = f.read()
    except FileNotFoundError:
        print(f"Template not found: {template_path}. Skipping.")
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

    # Per-page grouping logic
    if markdown_filename == 'datasets.md':
        subsection_col = 'Subsection' if 'Subsection' in df.columns else None
        if subsection_col is None:
            print("Warning: No 'Subsection' in datasets.csv; defaulting to 'Contexts (Environment & Climate)'.")
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
        # Group by Year from old → new
        if 'Year' not in df.columns:
            df['Year'] = ''
        df['_YearInt'] = df['Year'].apply(_parse_year)
        # Sort by Year ascending, then Title
        df = df.sort_values(by=['_YearInt', 'Title'], ascending=[True, True])
        # Known years
        years = [y for y in df['_YearInt'].dropna().unique()]
        for y in years:
            sub_df = df[df['_YearInt'] == y].copy()
            if not sub_df.empty:
                generated += f"\n\n<p class=\"paper-year\">{int(y)}</p>\n\n"
                for _, row in sub_df.iterrows():
                    generated += substitute_placeholders(block, row) + "\n\n"
        # Unknown year bucket
        unk_df = df[df['_YearInt'].isna()].copy()
        if not unk_df.empty:
            generated += "\n\n<p class=\"paper-year\">Unknown Year</p>\n\n"
            unk_df = unk_df.sort_values(['Title']).reset_index(drop=True)
            for _, row in unk_df.iterrows():
                generated += substitute_placeholders(block, row) + "\n\n"

    elif markdown_filename == 'conferences.md':
        # Group by Subsection ∈ {conference, journal}
        if 'Subsection' not in df.columns:
            df['Subsection'] = 'Journal'
        df['Subsection'] = df['Subsection'].apply(_standardize_subsection)
        order = ['Conference', 'Journal']
        labels = {'Conference': 'Conferences', 'Journal': 'Journals'}
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

print("\nAll pages processed.")
