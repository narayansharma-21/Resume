# Basic script to download resume and override existing one 

import requests
import shutil
import os

# URL of the PDF file you want to download
resume_url = "/Users/kingnutmegs/Documents/GitHub/Resume/Narayan Sharma Resume 2023.pdf"

# Path to your Downloads directory
downloads_dir = os.path.expanduser("~/Downloads")

# Define the name of the PDF file
pdf_file_name = "Narayan Sharma Resume.pdf"

# Download the PDF file
response = requests.get(resume_url, stream=True)

# Check if the download was successful (HTTP status code 200)
if response.status_code == 200:
    # Create the full path to the new PDF file in the Downloads directory
    pdf_path = os.path.join(downloads_dir, pdf_file_name)

    # Save the downloaded file to the Downloads directory
    with open(pdf_path, "wb") as pdf_file:
        shutil.copyfileobj(response.raw, pdf_file)

    # Remove the previous version of the resume (if it exists)
    previous_resume_path = os.path.join(downloads_dir, pdf_file_name)
    if os.path.exists(previous_resume_path):
        os.remove(previous_resume_path)

    print("Resume has been updated and saved to Downloads directory.")
else:
    print("Failed to download the resume PDF. Check the URL or your internet connection.")
