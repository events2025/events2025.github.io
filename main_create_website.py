import pandas as pd
import re

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

# Read the CSV file
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

# --- (Optional) classify datasets into subsections ---
event_keywords = [
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

mask = df['Type'].str.lower().str.contains('dataset', na=False)
df.loc[mask, 'Subsection'] = df[mask].apply(classify, axis=1)
df = df.sort_values(['Subsection','Title']).reset_index(drop=True)
# --- end classification block ---

# Substitute placeholders in a block of text
def substitute_placeholders(text, row):
    for ph in re.findall(r'\(\((.*?)\)\)', text):
        key = ph.strip()
        val = str(row.get(key,''))
        val = val.replace('\\','\\\\').replace('$','\\$')
        text = text.replace(f'(({ph}))', val)
    return text

# Iterate over each markdown file
for md_file, filter_term in files_to_process:
    print(f"Processing {md_file} (filter='{filter_term}')…")
    tpl_path = f'docs/{md_file}.template'
    try:
        md = open(tpl_path, encoding='utf-8').read()
    except FileNotFoundError:
        print(f"  Template not found: {tpl_path}, skipping.")
        continue

    START, STOP = '<!-- START -->', '<!-- STOP -->'
    i1, i2 = md.find(START), md.find(STOP, md.find(START))
    if i1 < 0 or i2 < 0:
        print(f"  No START/STOP in {md_file}, skipping.")
        continue

    block = md[i1+len(START):i2].strip()
    df_filt = df[df['Type'].str.lower().str.contains(filter_term, na=False)]
    generated = ''

    if md_file == 'datasets.md':
        for section in ['Events','Context','Other']:
            sec_df = df_filt[df_filt['Subsection'] == section]
            if sec_df.empty:
                continue
            generated += f"\n\n<p class=\"dataset-subsection\">{section}</p>\n\n"
            for _, row in sec_df.iterrows():
                html = substitute_placeholders(block, row)
                url = str(row.get('URL','')).strip()
                if url:
                    # Wrap the image tag in a link
                    html = re.sub(
                        r'(<img [^>]*>)',
                        fr'<a href="{url}">\1</a>',
                        html
                    )
                generated += html + "\n\n"
    else:
        for _, row in df_filt.iterrows():
            html = substitute_placeholders(block, row)
            url = str(row.get('URL','')).strip()
            if url:
                html = re.sub(
                    r'(<img [^>]*>)',
                    fr'<a href="{url}">\1</a>',
                    html
                )
            generated += html + "\n\n"

    # Rebuild and write out
    new_block = f"{START}\n{generated.strip()}\n{STOP}"
    out_md = md[:i1] + new_block + md[i2+len(STOP):]
    with open(f'docs/{md_file}', 'w', encoding='utf-8') as f:
        f.write(out_md)
    print(f"  → Updated docs/{md_file}")

print("Done.")
