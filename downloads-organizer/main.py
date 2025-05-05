#Downloads Organizer

from pathlib import Path
import shutil


origin_path = Path(r'C:\Users\Property Republic\Downloads')

file_list = list(Path.iterdir(origin_path))


folder_names = []
#STEP 1: Loop through each file in downloads folder:
for file in file_list:

    #STEP 2: Get the file_extension of file. 
    suffix = file.suffix
    if suffix not in folder_names:
        folder_names.append(suffix)




    #STEP 4: If folder with {file_extension} files exists in D drive, cut+paste to the folder
    #STEP 5: Else: Create folder {file_extension} files