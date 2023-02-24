#!/usr/bin/env python

import sys
import os
import glob
from time import sleep

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
        -v, --verbose   Verbose mode

    Args:
        -s, --source    Source directory
        -m, --masters   Master directory (optional, default: <Source directory>/Masters)
        -d, --dest      Destination directory (Default: <Source directory>/Selection)
"""
IMAGES_EXTENSIONS = ['.jpg', '.JPG', '.png', '.PNG', '.rw2', '.RW2']

def get_any_image_in_directory(source):
    output = []
    for extension in IMAGES_EXTENSIONS:
        output += glob.glob(os.path.join(source, f'*{extension}'))
    return output

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

    # check for verbose
    if '-v' in args or '--verbose' in args:
        verbose = True
    else:
        verbose = False

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
    source_files = get_any_image_in_directory(source)
    if verbose:
        print(f"Found {len(source_files)} files in {source}")

    # get the files in the master directory
    master_files = get_any_image_in_directory(masters)
    if verbose:
        print(f"Found {len(master_files)} files in {masters}")

    
    # compare files in source and master
    # if files are in master and in source, 
    # move source file to destination
    if verbose:
        print("Checking ")
    for file in source_files:
        # filename with extension
        file_name = os.path.basename(file)
        # filename lower case and no extension
        file_name_stip = file_name.lower().split('.')[0]
        master_files_names = [os.path.basename(f).lower().split('.')[0] for f in master_files]
        # master_files_names unique
        master_files_names = list(set(master_files_names))
        if verbose:
            print(f"{file_name}", end='\r')
            sleep(.02)
        copy = False
        for master_file_name in master_files_names:
            if file_name_stip in master_file_name:
                copy = True
                break
        if copy:
            destfile = os.path.join(dest, file_name)
            if verbose:
                print(f"\nMoving {file_name} to {destfile}")
            os.rename(file, destfile)
            
    # done
    print('\nDone')
    
