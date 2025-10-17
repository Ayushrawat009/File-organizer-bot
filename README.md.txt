## File Organizer (Python)

A simple yet powerful **Python automation script** that organizes your files into categorized folders based on file type and adds safe, timestamped filenames to prevent duplicates.

---

### Features
- Automatically categorizes files (e.g., Images, Documents, Videos, Others).  
- Renames files with a **creation/modification timestamp** for easy sorting.  
- Handles **filename conflicts** safely (adds `_1`, `_2`, etc.).  
- Creates required folders automatically.  
- Works on **Windows, macOS, and Linux**.

---

### How It Works
1. You provide a **source directory** (where your unorganized files are).  
2. You provide a **target directory** (where files will be organized).  
3. The script scans all files recursively and moves them into:
   - `exe/` ->  .`apps`
   - `images/` → `.jpg`, `.png`, etc.  
   - `documents/` → `.pdf`, `.docx`, etc.  
   - `videos/` → `.mp4`, `.avi`, etc.  
   - `other/` → any other file types  
4. Each moved file gets a **timestamped name** based on its creation date.

---

###  Example Usage
```bash
$ python file_organizer.py
Enter source directory: "E:\Downloads"
Enter target directory: "E:\Organized Files"
Proceed with organization? (Y/N): y
Moved: example.jpg -> images/2025-10-16-13-45-22-example.jpg
Moved: resume.pdf -> documents/2024-12-22-10-11-08-resume.pdf
Total files moved: 2
File organization completed!
```

---

###  Folder Structure
After running the script, your target folder will look like this:
```
Organized Files/
│
├── images/
├── documents/
├── videos/
└── other/
```

---

### Requirements
- Python 3.7 or higher  
- Works out-of-the-box (no external dependencies)

---

###  Customization
You can expand supported file types by editing the dictionary inside `categorize_file()`:
```python
categories = {
    ".jpg": "images",
    ".png": "images",
    ".pdf": "documents",
    ".docx": "documents",
    ".mp4": "videos",
    ".avi": "videos",
    ".zip": "archives",  # Example of a new category
}
```

---

###  Why Timestamped Filenames?
Timestamping helps track when files were created or downloaded and ensures **unique names** if files with the same name exist.

---

### 🧑‍💻 Author
**Ayush Rawat**  
Beginner–Intermediate Python Developer | Automation & Scripting Enthusiast  

---

