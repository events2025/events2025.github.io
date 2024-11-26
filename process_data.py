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


df['Image'] = df['Image'].replace('', '/assets/image/logo.jpg').replace(' ', '/assets/image/logo.jpg').fillna('/assets/image/logo.jpg')


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

# Function to replace placeholders with actual values
def substitute_placeholders(text, row):
    # Find all placeholders in the format ((ColumnName))
    placeholders = re.findall(r'\(\((.*?)\)\)', text)
    for placeholder in placeholders:
        # Trim any whitespace around the placeholder name
        key = placeholder.strip()
        # Replace the placeholder with the corresponding value if the column exists
        if key in row:
            value = str(row[key])
            # Escape backslashes and other special characters if necessary
            value = value.replace('\\', '\\\\').replace('$', '\\$')
            # Replace the placeholder in the text
            text = text.replace(f'(({placeholder}))', value)
        else:
            # If the column doesn't exist, replace with an empty string or handle as needed
            text = text.replace(f'(({placeholder}))', '')
    return text

# Iterate over each file and its corresponding filter term
for markdown_filename, filter_term in files_to_process:
    print(f"Processing {markdown_filename} with filter '{filter_term}'...")

    # Step 1: Read the Markdown template file
    template_file_path = f'docs/{markdown_filename}.template'
    try:
        with open(template_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"Template file not found: {template_file_path}. Skipping {markdown_filename}.")
        continue
    except Exception as e:
        print(f"An error occurred while reading {template_file_path}: {e}")
        continue

    # Step 2: Identify the text block between the START and STOP comments
    start_comment = '<!-- START -->'
    stop_comment = '<!-- STOP -->'

    start_index = markdown_content.find(start_comment)
    stop_index = markdown_content.find(stop_comment, start_index)

    if start_index != -1 and stop_index != -1:
        # Extract the paramtext block including the start and stop comments
        paramtext_block = markdown_content[start_index + len(start_comment):stop_index].strip()
    else:
        print(f"No paramtext block found in {markdown_filename} between '{start_comment}' and '{stop_comment}'. Skipping.")
        continue

    # Step 3: Apply the corresponding filter to the DataFrame
    filter_pattern = filter_term.lower()
    df_filtered = df[df['Type'].str.lower().str.contains(filter_pattern, na=False)]

    # Generate the new content by instantiating the paramtext block for each relevant CSV row
    generated_blocks = ''
    for idx, row in df_filtered.iterrows():
        block = substitute_placeholders(paramtext_block, row)
        generated_blocks += block + '\n\n'  # Add spacing between blocks if necessary

    # If there are zero entries, set generated_blocks to an empty string
    if df_filtered.empty:
        generated_blocks = ''

    # Replace the original paramtext block in the markdown content with the generated content
    if paramtext_block:
        # Reconstruct the full paramtext with comments
        new_paramtext = f"{start_comment}\n{generated_blocks.strip()}\n{stop_comment}"
        # Replace the old paramtext block with the new one
        markdown_content = (
            markdown_content[:start_index]
            + new_paramtext
            + markdown_content[stop_index + len(stop_comment):]
        )

    # Write the updated markdown content back to the file
    output_markdown_path = f'docs/{markdown_filename}'
    try:
        with open(output_markdown_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Successfully updated {output_markdown_path}.")
    except Exception as e:
        print(f"An error occurred while writing to {output_markdown_path}: {e}")

print("All specified Markdown files have been processed.")
