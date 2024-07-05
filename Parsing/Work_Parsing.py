import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
import re

def is_valid(url):
    """
    Check if the URL is valid.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Extract all internal and external links from the given URL.
    """
    urls = set()
    internal_urls = set()
    external_urls = set()

    domain_name = urlparse(url).netloc

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for tag in soup.find_all(['a', 'img']):  # Look for <a> tags and <img> tags
            if tag.name == 'a':
                href = tag.get('href')
            elif tag.name == 'img':
                src = tag.get('src')
                if src:
                    href = urljoin(url, src)
                else:
                    continue

            if href:
                parsed_href = urlparse(href)
                if parsed_href.scheme and parsed_href.netloc:
                    # Check if the URL points to an image or PDF file
                    if href.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.pdf')):
                        urls.add(href)
                        if domain_name in href:
                            internal_urls.add(href)
                        else:
                            external_urls.add(href)
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

    return internal_urls, external_urls

def download_file(url, folder_path):
    """
    Download a file from the given URL to the specified folder.
    """
    try:
        # Get the filename from the URL
        filename = url.split("/")[-1]
        # Decode the filename in case it's URL encoded
        filename = unquote(filename)
        
        # Check if the file is an image or PDF
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.pdf')
        if not any(ext in filename.lower() for ext in valid_extensions):
            print(f"Skipping non-image/PDF file: {filename}")
            return None
        
        # Construct the local file path
        local_path = os.path.join(folder_path, filename)
        
        # Create folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        # Download the file
        print(f"Downloading file from {url} to {local_path} ...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"File downloaded successfully.")
        return local_path
    except Exception as e:
        print(f"Failed to download file: {url}, Error: {e}")
        return None

def scan_website(url, folder_path):
    """
    Scan the website for internal and external links, and download specific files (images/PDFs).
    """
    if not os.path.exists(folder_path):
        # Create folder if it doesn't exist
        os.makedirs(folder_path)

    internal_urls, external_urls = get_all_website_links(url)

    print(f"Internal links ({len(internal_urls)}):")
    for link in internal_urls:
        print(link)
    
    print(f"\nExternal links ({len(external_urls)}):")
    for link in external_urls:
        print(link)

    # Download files with specific extensions
    for link in internal_urls:
        download_file(link, folder_path)

if __name__ == "__main__":
    # Request the URL to scan from the user
    url = input("Enter the URL of the website to scan: ").strip()
    # Construct the path to the Desktop folder
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    folder_path = os.path.join(desktop_path, "downloaded_files")
    scan_website(url, folder_path)
