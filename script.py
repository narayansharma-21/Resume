import shutil
import os

# Source file path (your local file)
source_file_path = "/Users/kingnutmegs/Documents/GitHub/Resume/Narayan Sharma Resume 2023.pdf"

# Destination directory (your Downloads directory)
downloads_dir = os.path.expanduser("~/Downloads")

# Define the name of the PDF file
pdf_file_name = "Narayan Sharma Resume.pdf"

# Create the full path to the destination file in the Downloads directory
destination_pdf_path = os.path.join(downloads_dir, pdf_file_name)

# Copy the source file to the destination directory
shutil.copyfile(source_file_path, destination_pdf_path)

print("Resume has been copied to Downloads directory.")
