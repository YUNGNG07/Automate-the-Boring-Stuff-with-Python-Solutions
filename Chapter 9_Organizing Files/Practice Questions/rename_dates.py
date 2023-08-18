"""
Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
"""
import shutil
import os
import re

# Create a regex that matches files with the American date format
date_pattern = re.compile(r'''^(.*?)
                          ((0|1)?\d)-
                          ((0|1|2|3)?\d)-
                          ((19|20)\d\d)
                          (.*?)$
                          ''', re.VERBOSE)

# Loop over the files in the working directory
for amer_filename in os.listdir('.'):
    mo = date_pattern.search(amer_filename)

    # Skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename
    before_part = mo.group(1)
    month_part = mo.group(2)
    day_part = mo.group(4)
    year_part = mo.group(6)
    after_part = mo.group(8)
