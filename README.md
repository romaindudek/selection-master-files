# SELECTION MASTER FILES    

If you take a lot of photos when you shoot and you want to keep the original picture you are working on, it can sometimes be painfull...

And if you let time pass, you might sometimes forget wich pictures you've worked on in your Master directory... wich is annoying if you have to compare the two dirs yourself when you have more than 20 files in Master dir an hundreds in source dir.

run:
```bash
selection.py -s <Source directory> [options]
```

And it will compare the file names in each dir and move any file witch name is in both source and
master dir into a new `<Selection>` dir.