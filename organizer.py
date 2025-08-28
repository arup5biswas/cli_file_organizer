import os
import shutil
import argparse
from colorama import Fore, Style, init

#Initializing colorama
init(autoreset=True)

def organize_files(src_dir):
    """Organizes files in the source directory into subdirectories."""
    if not os.path.isdir(src_dir):
        print(Fore.RED + f"Error: Source directory '{src_dir}' not found.")
        return
    
    #Defining categories
    CATEGORIES = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".jp2", ".j2k", ".jpf", ".avci"],
        "documents": [".pdf", ".docx", ".doc", ".txt", ".csv", ".md", ".pages", ".rtf", ".tex"],
        "audio": [".mp3", ".wav", ".mp2", ".flac", ".avi", ".m4a", ".ogg", ".mogg", ".wma"]
    }

    print(f"Organizing files in: {src_dir}\n")

    # Creating category directories if they don't exist
    for category in CATEGORIES:
        os.makedirs(os.path.join(src_dir, category), exist_ok=True)
    
    #Organizing files
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)

        if os.path.isfile(src_path):
            file_ext = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in CATEGORIES.items():
                if file_ext in extensions:
                    dest_path = os.path.join(src_dir,category, filename)
                    shutil.move(src_path, dest_path)
                    print(f"{Fore.GREEN}Moved: {filename} -> {category}/")
                    moved = True
                    break
            if not moved:
                print(f"{Fore.YELLOW}Skipped: {filename} (unknown file type)")

def main():
    parser = argparse.ArgumentParser(description="Organize files in a directory by their extension.")
    parser.add_argument("source_directory", type=str, help="The source directory to organize.")
    args = parser.parse_args()

    organize_files(args.source_directory)

if __name__ == "__main__":
    main()