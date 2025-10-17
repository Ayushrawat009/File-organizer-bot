import os
import shutil
from datetime import datetime
from pathlib import Path
import re  

def categorize_file(filepath):
    extension = Path(filepath).suffix.lower()
    categories = {
        ".jpg": "images",
        ".png": "images",
        ".pdf": "documents",
        ".docx": "documents",
        ".mp4": "videos",
        ".avi": "videos",
        ".exe": "apps"
    }
    return categories.get(extension.lower(), "other")

def creating_folders(target_directory):
    target_path = Path(target_directory)
    target_path.mkdir(parents=True, exist_ok=True)  
    for category in ["images", "documents", "videos", "other"]:
        (target_path / category).mkdir(exist_ok=True)

def get_safe_timestamped_name(filepath, original_filename): 
    try:
        timestamp = os.path.getctime(filepath)
    except OSError:
        timestamp = os.path.getmtime(filepath)
    file_date = datetime.fromtimestamp(timestamp)
    
    
    safe_date_str = re.sub(r'[:.]+', '-', file_date.isoformat().replace('T', '-'))
    safe_date_str = safe_date_str.split('.')[0] 
    
    name_without_ext = Path(original_filename).stem
    ext = Path(original_filename).suffix
    base_new_name = f"{safe_date_str}-{name_without_ext}{ext}"
    
    target_dir = Path(filepath).parent  
    counter = 1
    new_filename = base_new_name
    while (target_dir / new_filename).exists():
        new_filename = f"{safe_date_str}-{name_without_ext}_{counter}{ext}"
        counter += 1
    
    return new_filename

def sorting_files(source_directory, target_directory):
    source_path = Path(source_directory)
    target_path = Path(target_directory)
    moved_count = 0
    
    for root, _, files in os.walk(source_path):
        for filename in files:
            filepath = Path(root) / filename
            if filepath.is_file(): 
                file_category = categorize_file(filepath)
                category_dir = target_path / file_category
                new_filename = get_safe_timestamped_name(filepath, filename)
                target_file = category_dir / new_filename
                
                try:
                    shutil.move(str(filepath), str(target_file))
                    moved_count += 1
                    print(f"Moved: {filename} -> {file_category}/{new_filename}")
                except (OSError, shutil.Error) as e:
                    print(f"Error moving '{filename}': {e}")
    
    print(f"Total files moved: {moved_count}")

def main():
    source_input = input("Enter source directory: ").strip().strip('"\'')
    target_input = input("Enter target directory: ").strip().strip('"\'')
    
    source_directory = Path(source_input)
    target_directory = Path(target_input)
    
    if not source_directory.exists():
        print(f"Error: Source directory '{source_directory}' does not exist.")
        return
    
    if not source_directory.is_dir():
        print(f"Error: '{source_directory}' is not a directory.")
        return
    
    print(f"Source: {source_directory}")
    print(f"Target: {target_directory}")
    confirm = input("Proceed with organization? (Y/N): ").strip().lower()
    if confirm != 'Y':
        print("Aborted.")
        return
    
    creating_folders(target_directory)
    sorting_files(source_directory, target_directory)
    print("File organization completed!")

if __name__ == "__main__":
    main()
