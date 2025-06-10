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

# --- MODIFIED: Use existing subsection column for datasets ---
# Clean up the subsection column - handle NaN values and standardize capitalization
if 'subsection' in df.columns:
    # Fill NaN values with 'Other' and standardize capitalization
    df['subsection'] = df['subsection'].fillna('Other')
    
    # For datasets only, ensure subsection values are either 'Context' or 'Events' (case-insensitive)
    dataset_mask = df['Type'].str.lower().str.contains('dataset', na=False)
    
    # Standardize subsection values for datasets
    df.loc[dataset_mask, 'Subsection'] = df.loc[dataset_mask, 'subsection'].apply(
        lambda x: 'Context' if str(x).lower() in ['context'] 
                 else 'Events' if str(x).lower() in ['events', 'event'] 
                 else 'Other'
    )
    
    # For non-datasets, we don't need the Subsection column
    df.loc[~dataset_mask, 'Subsection'] = 'Other'
else:
    print("Warning: 'subsection' column not found in CSV. Adding default 'Other' subsection.")
    df['Subsection'] = 'Other'

# Sort globally so that datasets are grouped by subsection
df = df.sort_values(['Subsection', 'Title']).reset_index(drop=True)

# Define a function to clean the title
def clean_title(title):
    title = re.sub(r'[^\w\s-]', '', str(title))
    title = title.replace(' ', '_').lower()
    return title

# Process each row's image entry
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

    # Filter rows
    df_filt = df[df['Type'].str.lower().str.contains(filter_term.lower(), na=False)]

    # For datasets.md, group by Subsection using the existing subsection column
    generated = ''
    if markdown_filename == 'datasets.md':
        # Get unique subsections for datasets, prioritizing Context and Events
        subsections = df_filt['Subsection'].unique()
        # Sort to put Context and Events first, then Others
        subsection_order = []
        if 'Context' in subsections:
            subsection_order.append('Context')
        if 'Events' in subsections:
            subsection_order.append('Events')
        for section in sorted(subsections):
            if section not in ['Context', 'Events']:
                subsection_order.append(section)
        
        for section in subsection_order:
            sub_df = df_filt[df_filt['Subsection'] == section]
            if not sub_df.empty:
                generated += f"\n\n<p class=\"dataset-subsection\">{section}</p>\n\n"
                for _, row in sub_df.iterrows():
                    generated += substitute_placeholders(block, row) + "\n\n"
    else:
        # all others: simple flat list
        for _, row in df_filt.iterrows():
            generated += substitute_placeholders(block, row) + "\n\n"

    # rebuild the file content
    new_block = f"{start_c}\n{generated.strip()}\n{stop_c}"
    md = md[:i1] + new_block + md[i2+len(stop_c):]

    # write out
    out_path = f'docs/{markdown_filename}'
    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Updated {out_path}")
    except Exception as e:
        print(f"Error writing {out_path}: {e}")

print("All specified Markdown files have been processed.")
