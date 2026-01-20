# setup.py
"""
Data Setup Script for UIDAI Hackathon Project
Downloads required datasets from external source
"""

import os
import gdown  # pip install gdown
import zipfile

def download_data():
    """Download datasets from Google Drive"""
    
    # Create directories
    os.makedirs('data/raw/biometric_data', exist_ok=True)
    os.makedirs('data/processed', exist_ok=True)
    
    print("Downloading datasets from Google Drive...")
    
    # Google Drive file IDs (get from your shared links)
    files = {
        'aadhaar_overall.csv': 'https://drive.google.com/file/d/1r1MajFqNvfFDYCedTFoKLRaMB4A2DMxX/view?usp=drive_link',
        'aadhaar_statewise.csv': 'https://drive.google.com/file/d/1_oMyk-GE78JwP_aFAWUxfs-wkvP-VwmN/view?usp=drive_link'
    }
    
    for filename, file_id in files.items():
        output_path = f'data/raw/{filename}'
        if not os.path.exists(output_path):
            print(f"Downloading {filename}...")
            url = f'https://drive.google.com/uc?id={file_id}'
            gdown.download(url, output_path, quiet=False)
        else:
            print(f"{filename} already exists, skipping...")
    
    print("✅ Data download complete!")
    print("Run: python notebooks/01_exploration.ipynb")

if __name__ == "__main__":
    download_data()
