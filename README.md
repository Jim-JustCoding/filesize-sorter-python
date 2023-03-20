# File Sorter

This Python program sorts all the files in a given directory by **ascending file size.**

You may optionally enter in an extension with the `--extension` argument to only show files with the given extension.

Usage:

```bash
sortSize.py [--extension] [path]

# path | the path to the directory (eg. /home/user/...)
# -e, --extension | the file extension to sort only
```

- Files under 1MB are shown in White. Files between 1MB and 1GB are in Yellow, and the rest are in Blue.

- Giving an unknown file extension (eg. `.p5a`) will immediately close the program. Although `filename_extensions.txt` have **nearly** every known file extension, they's some... even weirder ones... [Source](https://gist.github.com/securifera/e7eed730cbe1ce43d0c29d7cd2d582f4)

- Format: [i] [filename] - [Date_Modified] | Size: [filesize]

- Dependency

  - [`Rich`](https://github.com/Textualize/rich)

  ```bash
  pip install rich
  ```

- Tested with Python 2.7+. Works with Linux and Windows.

- Possible features to add:

  - *Files names in print output can be clicked on to open its file using your default program*
  - *Remove `[path]` argument, instead opening a folder dialog window to select a directory. More user friendly.*

I've honestly have no idea why I even made this. Sudden inspiration, I guess.
