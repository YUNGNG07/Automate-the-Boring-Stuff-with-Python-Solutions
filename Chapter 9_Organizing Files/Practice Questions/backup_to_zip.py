"""
Copies an entire folder and its contents into a ZIP file whose filename increments.
"""

import zipfile
import os

def backup_to_zip(folder):
    """
    Backup the entire contents of 'folder' into a ZIP file.
    """
    # Make sure folder is absolute
    folder = os.path.abspath(folder)

    # Figure out the filename this code should use based on what files already exist
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number = number + 1

    # Create the ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for folder_name, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {folder_name}...')
        # Add the current folder to the ZIP file
        backup_zip.write(folder_name)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                # Do not backup the backup ZIP files
                continue
            backup_zip.write(os.path.join(folder_name, filename))
    backup_zip.close()
    print('Done.')

backup_to_zip('C:\\delicious')


