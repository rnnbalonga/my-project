#Downloads Organizer

from pathlib import Path
import shutil


origin_path = Path(r'C:\Users\Property Republic\Downloads')

file_list = list(Path.iterdir(origin_path))


file_types = {}

#Clean up the values of the file_types list
def clean_suffix(suffix):
    if suffix.startswith('.'):
        return suffix[1:]
    elif suffix == "":
        return "Folders"
    
#STEP 3: For each file_type, make a folder in the D drive
def make_folder(folder_name):
    destination_path = Path(f'{origin_path}\\{folder_name}')
    try:
        destination_path.mkdir()
        print(f"Directory '{destination_path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{destination_path}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{destination_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def cut_and_paste_file(file, suffix):
    source = file
    destination = origin_path / file_types[suffix]

    shutil.move(source, destination)

    

#STEP 1: Loop through each file in downloads folder:
for file in file_list:

    #STEP 2: Get the file_extension of file. 
    suffix = file.suffix
    if suffix not in file_types:
        #Append to dictionary where key=suffix and #value == cleaned version of key (e.g. no leading '.')
        file_types[suffix] = clean_suffix(suffix)
        #Create a folder
        make_folder(file_types[suffix])
    
    cut_and_paste_file(file)




