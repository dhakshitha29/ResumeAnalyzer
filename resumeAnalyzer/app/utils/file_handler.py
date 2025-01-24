import os

def save_file(file, upload_folder):
    # Ensure the upload folder exists
    os.makedirs(upload_folder, exist_ok=True)
    
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    print(f"File saved to: {file_path}")

    return file_path
