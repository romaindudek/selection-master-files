# SELECTION MASTER FILES    

If you take a lot of photos when you shoot and you want to keep the original picture you are working on, it can sometimes be painfull...

And if you let time pass between the shooting and post production work, you might sometimes forget wich pictures you've allready worked on in your Master directory... Wich is annoying if you have to compare the two dirs yourself when you have more than 20 files in Master dir an hundreds in source dir.

## Usage

Assuming your default python is python3, run:
```bash
python selection.py -s <Source directory> [options]
```

And it will compare the file names in each dir and move any file witch name is in both source and
master dir into a new `<Selection>` dir.

If you have a serarate directory for your RAW files, you can use the -rd option, note that the raw file dir MUST BE INSIDE the source dir.

example:
```bash
./selection.py -s '/Volumes/Crucial/Shooting_2023-02-08/' -v -rd RAW
```
After proccessing, you'll have something like this:<br>
`Selection` and `Selection/RAW/` were created and original picture files have been moved  to thoses dirs
```bash
Shooting_2023-02-08/
├── Masters
│   ├── PGX_0429.JPG
│   ├── PGX_0433.JPG
│   ├── PGX_0434.JPG
│   ├── PGX_0429.RW2
│   ├── PGX_0433.RW2
│   └── PGX_0434.RW2
├── (...)
├── PGX_0419.JPG
├── PGX_0420.JPG
├── PGX_0421.JPG
├── PGX_0422.JPG
├── PGX_0427.JPG
├── PGX_0428.JPG
├── PGX_0430.JPG
├── PGX_0431.JPG
├── PGX_0432.JPG
├── (...)
├── RAW
│   ├── (...)
│   ├── PGX_0419.RW2
│   ├── PGX_0420.RW2
│   ├── PGX_0421.RW2
│   ├── PGX_0422.RW2
│   ├── PGX_0427.RW2
│   ├── PGX_0428.RW2
│   ├── PGX_0430.RW2
│   ├── PGX_0431.RW2
│   ├── PGX_0432.RW2
│   └── (...)
└── Selection
    ├── PGX_0429.JPG
    ├── PGX_0433.JPG
    ├── PGX_0434.JPG
    └── RAW
        ├── PGX_0429.RW2
        ├── PGX_0433.RW2
        └── PGX_0434.RW2
```
## Workflow improvement
Now, your workflow can simply be :
- Copy any file you need to process inside a "Master" (or whatever you want) directory, work on it won't affect original files.
- If you have a lot of files to work on and you want to separate the files you allready worked on from the other original files, simply run selection.py

## Requirements
Python3 is needed, no additional packages.