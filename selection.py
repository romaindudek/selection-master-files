#!/usr/bin/env python

import sys
import os
import glob
from time import sleep

__author__ = 'Romain Dudek'
__version__ = '1.0.1'
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
        -s, --source        Source directory
        -m, --masters       Master directory (optional, default: <Source directory>/Masters)
        -d, --dest          Destination directory (optional, default: <Source directory>/Selection)
        -rd, --raw-dir      Separate raw directory (optional, relative to Source directory, no default)
"""

images_extensions =[ ".JPG", ".PNG", ".GIF", ".BMP", ".TIFF", ".TIF"]
images_extensions_low = [ext.lower() for ext in images_extensions]
IMAGES_EXTENSIONS = images_extensions + images_extensions_low

raw_extensions = [".NEF", ".CR2", ".ARW", ".ORF", ".RW2", ".PEF"]
raw_extensions_low = [ext.lower() for ext in raw_extensions]
RAW_IMAGES_EXTENSIONS = raw_extensions + raw_extensions_low
 

def get_any_image_in_directory(source, source_raw=None):
    """Returns a list of all images in a directory"""
    output = []
    if not source_raw:
        for extension in IMAGES_EXTENSIONS + RAW_IMAGES_EXTENSIONS:
            output += glob.glob(os.path.join(source, f'*{extension}'))
    else:
        for extension in IMAGES_EXTENSIONS:
            output += glob.glob(os.path.join(source, f'*{extension}'))
        for extension in RAW_IMAGES_EXTENSIONS:
            output += glob.glob(os.path.join(source_raw, f'*{extension}'))
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

    # check for raw directory
    if '-rd' in args:
        raw_dir_name = args[args.index('-rd') + 1]
    elif '--raw-dir' in args:
        raw_dir_name = args[args.index('--raw-dir') + 1]
    else:
        raw_dir_name = None

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
        if verbose:
            print(f"Creating {dest}")
        os.makedirs(dest)
    
    # check if raw directories exists and create dest_raw if needed
    if raw_dir_name:
        source_raw = os.path.join(source, raw_dir_name)
        if not os.path.exists(source_raw):
            print('ERROR: RAW directory does not exist')
            sys.exit(1)
        else:
            dest_raw = os.path.join(dest, raw_dir_name)
            if not os.path.exists(dest_raw):
                if verbose:
                    print(f"Creating {dest_raw}")
                os.makedirs(dest_raw)
    else:
        source_raw = None
        dest_raw = None
            
    # get the files in the source directory
    source_files = get_any_image_in_directory(source, source_raw)
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
            # slows the printing down to make it easier to see what's going on
            sleep(.01)
        copy = False
        for master_file_name in master_files_names:
            if file_name_stip in master_file_name:
                copy = True
                break
        if copy:
            filename_ext = os.path.splitext(file_name)[1]
            if filename_ext in RAW_IMAGES_EXTENSIONS and dest_raw is not None:
                destfile = os.path.join(dest_raw, file_name)
            else:
                destfile = os.path.join(dest, file_name)
            if verbose:
                print(f"\nMoving {file_name} to {destfile}")
            os.rename(file, destfile)
    if verbose:
        print()
    # done
    print('Done')
    
