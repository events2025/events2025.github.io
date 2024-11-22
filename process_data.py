import pandas as pd
import re

# Step 1: Read the Markdown file
markdown_file_path = 'docs/websites.md'
with open(markdown_file_path + ".template", 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Step 2: Identify the text block between the START and STOP comments called paramtext
start_comment = '<!-- START -->'
stop_comment = '<!-- STOP -->'

start_index = markdown_content.find(start_comment)
stop_index = markdown_content.find(stop_comment, start_index)

if start_index != -1 and stop_index != -1:
    # Extract the paramtext block including the start and stop comments
    paramtext_block = markdown_content[start_index + len(start_comment):stop_index].strip()
else:
    print("No paramtext block found between <!-- START --> and <!-- STOP -->.")
    paramtext_block = ''

# Step 3: Read the CSV file
csv_file_path = 'data/input.csv'
df = pd.read_csv(csv_file_path, encoding='utf-8')

# Filter rows where Type equals 'Method/Paper'
df_papers = df[df['Type'] == 'Method/Paper']

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

# Generate the new content by instantiating the paramtext block for each relevant CSV row
generated_blocks = ''
for idx, row in df_papers.iterrows():
    block = substitute_placeholders(paramtext_block, row)
    generated_blocks += block + '\n\n'  # Add spacing between blocks if necessary

# If there are zero entries, set generated_blocks to an empty string
if df_papers.empty:
    generated_blocks = ''

# Replace the original paramtext block in the markdown content with the generated content
if paramtext_block:
    # Reconstruct the full paramtext with comments
    new_paramtext = f"{start_comment}\n{generated_blocks.strip()}\n{stop_comment}"
    # Replace the old paramtext block with the new one
    markdown_content = markdown_content[:start_index] + new_paramtext + markdown_content[stop_index + len(stop_comment):]

# Write the updated markdown content back to the file
with open(markdown_file_path, 'w', encoding='utf-8') as f:
    f.write(markdown_content)

print("Markdown file has been successfully updated.")
