#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists('text-file.txt') :
    # get the path to the file in the current directory
    src = path.realpath('text-file.txt')
        
    # # let's make a backup copy by appending "bak" to the name
    dest = src + ".copy2"
    # # now use the shell to make a copy of the file
    shutil.copy(src, dest)
    # shutil.copy2(src, dest)

    # # rename the original file
    new_file_name = "text-file-new-file.text"
    os.rename(dest, new_file_name)
    
    # now put things into a ZIP archive
    root_dir, tail = path.split(new_file_name)
    print(shutil.make_archive("archive", "zip", root_dir))

    # more fine-grained control over ZIP files
    with ZipFile("text-zip.zip", 'w') as new_zip :
        new_zip.write('text-file.txt')
        # new_zip.write('text-file.txt')
        new_zip.write('text-file-new-file.text')
      