from pathlib import Path
import re
import shutil
#--------------------------------------------------------#
# Variable - Change to match your requirement
#--------------------------------------------------------#
# Matches "26. MusicPlayer App - MediaPlayer , Read from Local Storage & Interface"
# Returns "26" and "MusicPlayer App - MediaPlayer , Read from Local Storage & Interface"
folder_regex = re.compile(r'(\d{1,2})\. (.*)')

# Defaults to current folder, change to manually set your source folder.
parent_folder = Path(__file__).parent.absolute()
file_extension = "*.mp4"
#--------------------------------------------------------#

#--------------------------------------------------------#
# Constants - DO NOT CHANGE
#--------------------------------------------------------#
# Creates a folder called "consolidated" inside the parent folder.
CONSOLIDATED_FOLDER = parent_folder/"consolidated"
#--------------------------------------------------------#

Path(CONSOLIDATED_FOLDER).mkdir(exist_ok=True)
print(f'Created {CONSOLIDATED_FOLDER}')

# Purely for visual indication purposes
count = 0
for src in Path(__file__).parent.absolute().rglob(file_extension):
    if folder_regex.match(src.parent.name):
        count = count + 1

done_count = 0
for src in Path(__file__).parent.absolute().rglob(file_extension):
    if folder_regex.match(src.parent.name):
        prefix = folder_regex.match(src.parent.name).group(1).zfill(2)
        # Replacing '. ' with an underscore
        suffix = src.name.replace('. ', '_')

        # Replacing the rest of the white spaces with underscores
        suffix = suffix.replace(' ', '_')

        # Creating target file path
        dest = f"{CONSOLIDATED_FOLDER}/{prefix}_{suffix}"
        shutil.copy(src, dest)

        done_count = done_count + 1

        if done_count < count:
            print(f"Consolidated ({done_count}/{count})", end='\r')
        else:
            print(f"Consolidated ({done_count}/{count})", end='\n')

print("Done")
