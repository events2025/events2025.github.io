import pandas as pd
import re
import os
import shutil

# Define the mapping between Markdown files and their corresponding filter terms
files_to_process = [
    ('websites.md', 'website'),
    ('datasets.md', 'dataset'),
    ('tools.md', 'tool'),
    ('conferences.md', 'conference'),
    ('methods.md', 'method'),
    ('tutorials.md', 'tutorial')
]

# Path to the CSV file
csv_file_path = 'data/Add Item to "Events in Context" Knowledge Base.csv'

# Read the CSV file once
try:
    df = pd.read_csv(csv_file_path, encoding='utf-8')
except FileNotFoundError:
    print(f"CSV file not found at path: {csv_file_path}")
    exit(1)
except pd.errors.EmptyDataError:
    print("CSV file is empty.")
    exit(1)
except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")
    exit(1)

# --- NEW: classify datasets into subsections ---
event_keywords   = [
    'crime','collision','accident','911','police','fire','earthquake',
    'conflict','hurricane','flood','wildfire','protest','disease','covid',
    'disaster','traffic','call data'
]
context_keywords = [
    'population','demographics','census','density','land cover','landuse',
    'elevation','terrain','satellite','road','rail','boundary','admin',
    'weather','climate','geology','vegetation'
]

def classify(row):
    text = (str(row.get('Title','')) + ' ' + str(row.get('Description',''))).lower()
    if any(kw in text for kw in event_keywords):
        return 'Events'
    elif any(kw in text for kw in context_keywords):
        return 'Context'
    else:
        return 'Other'

# Only classify rows whose Type contains 'dataset'
mask = df['Type'].str.lower().str.contains('dataset', na=False)
df.loc[mask, 'Subsection'] = df[mask].apply(classify, axis=1)

# Sort globally so that datasets are grouped
df = df.sort_values(['Subsection','Title']).reset_index(drop=True)
# --- end classification block ---

# Define a function to clean the title
def clean_title(title):
    title = re.sub(r'[^\w\s-]', '', str(title))
    title = title.replace(' ', '_').lower()
    return title

# Process each row’s image entry
for idx, row in df.iterrows():
    image = str(row.get('Image',''))
    if "assets/images/thumb" not in image:
        title = row['Title']
        cleaned_title = clean_title(title)
        new_image_path = f'assets/images/thumb/{cleaned_title}.jpg'
        df.at[idx, 'Image'] = "/" + new_image_path
        src = 'assets/images/logo.jpg'
        dst = new_image_path
        if not os.path.exists(dst):
            try:
                shutil.copy(src, dst)
            except Exception as e:
                print(f"Error copying image for '{title}': {e}")

# Substitute placeholders in the template
def substitute_placeholders(text, row):
    placeholders = re.findall(r'\(\((.*?)\)\)', text)
    for placeholder in placeholders:
        key = placeholder.strip()
        value = str(row.get(key, ''))
        # escape backslashes and dollar signs
        value = value.replace('\\', '\\\\').replace('$', '\\$')
        text = text.replace(f'(({placeholder}))', value)
    return text

# Iterate over each markdown file
for markdown_filename, filter_term in files_to_process:
    print(f"Processing {markdown_filename} with filter '{filter_term}'...")
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
        print(f"No START/STOP in {markdown_filename}. Skipping.")
        continue
    block = md[i1+len(start_c):i2].strip()

    # Filter rows for this section
    df_filt = df[df['Type'].str.lower().str.contains(filter_term.lower(), na=False)]

    generated = ''
    if markdown_filename == 'datasets.md':
        # Datasets get grouped by subsection
        for section in ['Events','Context','Other']:
            sub_df = df_filt[df_filt['Subsection'] == section]
            if not sub_df.empty:
                generated += f"\n\n<p class=\"dataset-subsection\">{section}</p>\n\n"
                for _, row in sub_df.iterrows():
                    html = substitute_placeholders(block, row)
                    # Remove any fixed width/height so images stay at their intrinsic size
                    html = re.sub(r'width\s*:\s*\d+px\s*;?', '', html)
                    html = re.sub(r'height\s*:\s*\d+px\s*;?', '', html)
                    url = str(row.get('URL','')).strip()
                    if url:
                        # Wrap the first <img> tag in a link
                        html = re.sub(
                            r'(<img [^>]*>)',
                            fr'<a href="{url}">\1</a>',
                            html
                        )
                    generated += html + "\n\n"
    else:
        # All other pages: flat list
        for _, row in df_filt.iterrows():
            html = substitute_placeholders(block, row)
            # Remove any fixed width/height so images stay at their intrinsic size
            html = re.sub(r'width\s*:\s*\d+px\s*;?', '', html)
            html = re.sub(r'height\s*:\s*\d+px\s*;?', '', html)
            url = str(row.get('URL','')).strip()
            if url:
                html = re.sub(
                    r'(<img [^>]*>)',
                    fr'<a href="{url}">\1</a>',
                    html
                )
            generated += html + "\n\n"

    # Rebuild the file content with the new block
    new_block = f"{start_c}\n{generated.strip()}\n{stop_c}"
    md = md[:i1] + new_block + md[i2+len(stop_c):]

    # Write out the updated markdown
    out_path = f'docs/{markdown_filename}'
    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Updated {out_path}")
    except Exception as e:
        print(f"Error writing {out_path}: {e}")

print("All specified Markdown files have been processed.")
