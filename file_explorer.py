# Name:   file_explorer.py
# Date:   2025-09-08
# Author: Ethan L'Heureux

from pathlib import Path
import sys

d = Path(sys.argv[1])

for f in d.iterdir():
    if f.is_file():
        s = f.stat().st_size # Gets size of file or folder/directory.
        if f.suffix:         # Check if file has an extension.
            ext = f.suffix   # Get the extension w/ the dot.
            ext = ext[1:]    # Remove the dot at the beginning.
        else:
            ext = "-"        # If no extension, use "-".
        print(f, "--", "file", "-", s, "-", ext)
    elif f.is_dir():
        print(f, "--", "dir", "-", "-", "-")
    else:
        print(f, "--", "other", "-", "-", "-")

# TO RUN
# use cmd:
# python file_explorer.py /workspaces/cs-310-file-system-explorer