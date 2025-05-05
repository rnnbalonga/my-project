from pathlib import Path
import shutil

origin_path = Path(r'C:\Users\Property Republic\Downloads')
file_list = list(origin_path.iterdir())

file_types = {}

def clean_suffix(suffix):
    if suffix.startswith('.'):
        return suffix[1:] or "Unknown"
    elif suffix == "":
        return "Folders"
    return suffix

def make_folder(folder_name):
    destination_path = Path(f'D:\\{folder_name}')
    try:
        destination_path.mkdir(exist_ok=True)
        print(f"Directory '{destination_path}' is ready.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{destination_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def cut_and_paste_file(file, folder_name):
    source = file
    destination = Path(f'D:\\{folder_name}\\{file.name}')
    try:
        shutil.move(str(source), str(destination))
        print(f"Moved '{source.name}' to '{folder_name}' folder.")
    except Exception as e:
        print(f"Error moving '{source.name}': {e}")

for file in file_list:
    if file.is_dir():
        suffix = ""
    else:
        suffix = file.suffix

    folder_name = clean_suffix(suffix)

    if suffix not in file_types:
        file_types[suffix] = folder_name
        make_folder(folder_name)

    cut_and_paste_file(file, folder_name)
