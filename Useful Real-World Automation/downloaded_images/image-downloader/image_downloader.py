import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Website URL
url = "https://news.ycombinator.com"

# Folder to save images
folder = "downloaded_images"
os.makedirs(folder, exist_ok=True)

# Get webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all image tags
images = soup.find_all("img")

print(f"Found {len(images)} images")

for i, img in enumerate(images):
    img_url = img.get("src")

    if not img_url:
        continue

    # Convert relative URL to full URL
    img_url = urljoin(url, img_url)

    try:
        img_data = requests.get(img_url).content
        file_path = os.path.join(folder, f"image_{i+1}.jpg")

        with open(file_path, "wb") as f:
            f.write(img_data)

        print(f"Downloaded: {file_path}")

    except Exception as e:
        print("Error downloading:", img_url)

print("Download completed.")