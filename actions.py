import os
import shutil
import time
from config import DOWNLOADS_FOLDER, FILE_TYPES

def organize_by_type():
    """Move files into subfolders named after categories defined in FILE_TYPES."""
    for category, extensions in FILE_TYPES.items():
        category_folder = os.path.join(DOWNLOADS_FOLDER, category)
        os.makedirs(category_folder, exist_ok=True)

        for filename in os.listdir(DOWNLOADS_FOLDER):
            if filename.startswith('.'):
                continue  # Skip hidden/system files
            file_path = os.path.join(DOWNLOADS_FOLDER, filename)
            if not os.path.isfile(file_path):
                continue
            if any(filename.lower().endswith(ext) for ext in extensions):
                target = os.path.join(category_folder, filename)
                try:
                    shutil.move(file_path, target)
                except Exception as e:
                    print(f"Failed to move {filename}: {e}")
    print("Organized files by type.")

def delete_files_older_than(days: int = 30):
    """Delete files older than the specified number of days."""
    now = time.time()
    cutoff = now - days * 86400
    deleted = []
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)
        if not os.path.isfile(file_path):
            continue
        try:
            if os.path.getmtime(file_path) < cutoff:
                os.remove(file_path)
                deleted.append(filename)
        except Exception as e:
            print(f"Failed to delete {filename}: {e}")
    print(f"Deleted files older than {days} days: {deleted}")

def move_files_by_extension(extension: str, target_folder: str):
    """Move files with a given extension to a target subfolder."""
    extension = extension.lower()
    if not extension.startswith('.'):
        print("Extension should start with a dot (e.g. .pdf)")
        return
    target_dir = os.path.join(DOWNLOADS_FOLDER, target_folder)
    os.makedirs(target_dir, exist_ok=True)
    moved = []
    for filename in os.listdir(DOWNLOADS_FOLDER):
        file_path = os.path.join(DOWNLOADS_FOLDER, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(extension):
            try:
                shutil.move(file_path, os.path.join(target_dir, filename))
                moved.append(filename)
            except Exception as e:
                print(f"Failed to move {filename}: {e}")
    print(f"Moved {len(moved)} '{extension}' file(s) to {target_folder}/: {moved}")
