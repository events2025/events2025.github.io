import pandas as pd
import requests
from PIL import Image
import os
import re

# Load the CSV file
csv_file_path = 'data/Add Item to "Events in Context" Knowledge Base.csv'  # Replace with your actual file path
output_csv_path = 'data/data_processed.csv'
df = pd.read_csv(csv_file_path)

# Paths for default image and thumbnail folder
default_image_path = '/assets/images/logo.jpg'
thumbnail_folder = '/assets/images/thumb/'

# Create thumbnail folder if not exists
os.makedirs(thumbnail_folder, exist_ok=True)

# Function to clean and format title
def clean_title(title):
    # Remove special characters and spaces, replace with underscores
    return re.sub(r'[^\w\s]', '', title).replace(' ', '_')

# Function to check if URL is valid
def is_valid_url(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        content_type = response.headers.get('Content-Type', '')
        return response.status_code == 200 and 'image' in content_type
    except:
        return False

# Function to download and save an image
def download_and_save_image(url, save_path):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            img = Image.open(response.raw)
            img.convert('RGB').save(save_path, 'JPEG')
            return True
    except:
        pass
    return False

# Iterate over rows
for index, row in df.iterrows():
    image_entry = str(row.get('Image', ''))
    title = str(row.get('Title', '')).strip()

    # Skip rows with empty title
    if not title:
        continue

    # Clean the title
    cleaned_title = clean_title(title)
    save_path = os.path.join(thumbnail_folder, f'{cleaned_title}.jpg')

    # Check if the Image entry contains the desired path
    if "/assets/images/thumb/" in image_entry:
        continue  # No action needed for these rows

    # Check if the Image entry is a valid URL and try to download
    if is_valid_url(image_entry):
        if download_and_save_image(image_entry, save_path):
            # Update Image column to the saved path
            df.at[index, 'Image'] = save_path
            continue

    # If not valid or downloadable, use the default image
    try:
        default_img = Image.open(default_image_path)
        default_img.save(save_path, 'JPEG')
        df.at[index, 'Image'] = save_path
    except Exception as e:
        print(f"Error handling default image for row {index}: {e}")

# Save the processed DataFrame
df.to_csv(output_csv_path, index=False)
print(f"Processing complete. Processed file saved as {output_csv_path}.")
