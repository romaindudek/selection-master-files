#!/usr/bin/env python

import sys
import os
import glob

# grab current directory

__author__ = 'Romain Dudek'
__version__ = '1.0.0'
__date__ = '2023-02-01'
__license__ = 'MIT'
__description__ = "Check if Source images files (from a Source directory)\n        are in a Master directory, and copy them to a Selection directory"
__usage__ = 'selection.py -s <Source directory> [options]'

__help__ = f"""
    HELP
    Description: 
        {__description__}
    Usage:
        {__usage__}
    
    Options:
        -h, --help      Show this help message

    Args:
        -s, --source    Source directory
        -m, --masters   Master directory (optional, default: <Source directory>/Masters)
        -d, --dest      Destination directory (Default: <Source directory>/Selection)
"""

if __name__ == '__main__':

    # grab the args
    args = sys.argv[1:]

    # check for help
    if '-h' in args or '--help' in args or len(args) == 0:
        print(__help__)
        sys.exit(0)

    # check for source
    if '-s' in args:
        source = args[args.index('-s') + 1]
    elif '--source' in args:
        source = args[args.index('--source') + 1]
    else:
        print('ERROR: No source directory specified (mandatory)')
        print(__help__)
        sys.exit(1)
    
    # check for master
    if '-m' in args:
        masters = args[args.index('-m') + 1]
    elif '--masters' in args:
        masters = args[args.index('--masters') + 1]
    else:
        masters = os.path.join(source, 'Masters')
    
    # check for destination
    if '-d' in args:
        dest = args[args.index('-d') + 1]
    elif '--dest' in args:
        dest = args[args.index('--dest') + 1]
    else:
        dest = os.path.join(source, 'Selection')

    # check if source exists
    if not os.path.exists(source):
        print('ERROR: Source directory does not exist')
        sys.exit(1)

    # check if master exists
    if not os.path.exists(masters):
        print('ERROR: Master directory does not exist')
        sys.exit(1)

    # check if destination exists
    if not os.path.exists(dest):
        os.makedirs(dest)

    # get the files in the source directory
    # extension can be any image exension
    jpg_files = glob.glob(os.path.join(source, '*.jpg'))
    JPG_files = glob.glob(os.path.join(source, '*.JPG'))
    png_files = glob.glob(os.path.join(source, '*.png'))
    PNG_files = glob.glob(os.path.join(source, '*.PNG'))
    files = jpg_files + JPG_files + png_files + PNG_files

    # files = glob.glob(os.path.join(source, '*.JPG'))
    print(f"Found {len(files)} files in {source}")

    # get the files in the master directory
    #master_files = glob.glob(os.path.join(masters, '*.jpg')) + glob.glob(os.path.join(masters, '*.JPG'))
    jpg_files = glob.glob(os.path.join(masters, '*.jpg'))
    JPG_files = glob.glob(os.path.join(masters, '*.JPG'))
    png_files = glob.glob(os.path.join(masters, '*.png'))
    PNG_files = glob.glob(os.path.join(masters, '*.PNG'))
    master_files = jpg_files + JPG_files + png_files + PNG_files

    
    # compare files in source and master
    # if files are in master and in source, move source file to destination
    for file in files:
        # filename with extension
        file_name = os.path.basename(file)
        # filename lower case and no extension
        file_name_stip = file_name.lower().split('.')[0]
        master_files_names = [os.path.basename(f).lower().split('.')[0] for f in master_files]
        # master_files_names unique
        master_files_names = list(set(master_files_names))
        print(f"Checking {file_name}")
        copy = False
        for master_file_name in master_files_names:
            if file_name_stip in master_file_name:
                copy = True
                break
        if copy:
            destfile = os.path.join(dest, file_name)
            print(f"Moving {file_name} to {destfile}")
            os.rename(file, destfile)
            
    # done
    print('Done')
    
