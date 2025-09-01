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
    ('methods.md', 'data/papers_methods.csv'),
    ('conferences.md', 'data/venues_conference_journals.csv'),
]

# Helpers
def clean_title(title: str) -> str:
    title = re.sub(r'[^\w\s-]', '', str(title))
    return title.replace(' ', '_').lower()

def substitute_placeholders(text: str, row: pd.Series) -> str:
    placeholders = re.findall(r'\(\((.*?)\)\)', text)
    for placeholder in placeholders:
        key = placeholder.strip()
        value = str(row.get(key, ''))
        # escape a couple latex-y chars so templates don't break
        value = value.replace('\\', '\\\\').replace('$', '\\$')
        text = text.replace(f'(({placeholder}))', value)
    return text

def ensure_image_thumb(row: pd.Series) -> str:
    """Ensure Image points to /assets/images/thumb/<cleaned>.jpg, copying a default if missing."""
    os.makedirs('assets/images/thumb', exist_ok=True)
    img = str(row.get('Image', ''))
    if "assets/images/thumb" in img:
        # normalize to leading slash
        return img if img.startswith("/") else "/" + img
    title = row.get('Title', 'item')
    cleaned = clean_title(title)
    new_rel = f"assets/images/thumb/{cleaned}.jpg"
    new_abs = new_rel  # same repo relative path
    src = 'assets/images/logo.jpg'   # default placeholder image
    if not os.path.exists(new_abs):
        try:
            shutil.copy(src, new_abs)
        except Exception as e:
            print(f"Error copying default image for '{title}': {e}")
    return "/" + new_rel

# Render each markdown from its CSV
for markdown_filename, csv_path in files_to_process:
    print(f"\n==> Building {markdown_filename} from {csv_path}")

    # Read the CSV for this page
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

    # Normalize required columns minimally (do NOT rename — templates expect exact keys)
    # Fill missing Image with generated thumb; sort for stable output
    if 'Title' not in df.columns:
        print(f"Warning: 'Title' column missing in {csv_path}. Output order may be arbitrary.")
        df['_TitleSort'] = range(len(df))
        sort_cols = ['_TitleSort']
    else:
        sort_cols = ['Title']

    # Datasets-specific handling for Subsection grouping
    if markdown_filename == 'datasets.md':
        # ensure Subsection exists
        subsection_col = 'Subsection' if 'Subsection' in df.columns else ('subsection' if 'subsection' in df.columns else None)
        if subsection_col is None:
            print("Warning: No 'Subsection' column found; defaulting to 'Contexts (Environment & Climate)'.")
            df['Subsection'] = 'Contexts (Environment & Climate)'
        elif subsection_col != 'Subsection':
            df['Subsection'] = df[subsection_col]

        # Standardize dataset subsections (keep 3 contexts + Events)
        context_categories = [
            'Contexts (Environment & Climate)',
            'Contexts (Misc Data & APIs)',
            'Contexts (Population Data & Mobility)',
        ]
        df['Subsection'] = df['Subsection'].apply(
            lambda x: 'Events' if str(x).strip().lower() in {'event', 'events'} else str(x)
        )

        # Sort by Subsection then Title
        sort_cols = (['Subsection'] + sort_cols) if 'Title' in df.columns else ['Subsection']

    # Ensure Image column exists and populate thumbs
    if 'Image' not in df.columns:
        df['Image'] = ''
    df['Image'] = df.apply(ensure_image_thumb, axis=1)

    # Sorting
    try:
        df = df.sort_values(sort_cols).reset_index(drop=True)
    except Exception:
        pass  # if sort columns are inconsistent, just keep original order

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

    # Build generated content
    generated = ''
    if markdown_filename == 'datasets.md':
        sections_to_show = [
            'Contexts (Environment & Climate)',
            'Contexts (Misc Data & APIs)',
            'Contexts (Population Data & Mobility)',
            'Events',
        ]
        for section in sections_to_show:
            sub_df = df[df['Subsection'] == section] if 'Subsection' in df.columns else pd.DataFrame([])
            if not sub_df.empty:
                generated += f"\n\n<p class=\"dataset-subsection\">{section}</p>\n\n"
                for _, row in sub_df.iterrows():
                    generated += substitute_placeholders(block, row) + "\n\n"
    else:
        for _, row in df.iterrows():
            generated += substitute_placeholders(block, row) + "\n\n"

    # Rebuild and write out page
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
