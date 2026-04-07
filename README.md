# Move Duplicates Script

A simple Python script that finds duplicate files in a folder (by MD5 hash) and moves them into a `duplicates/` subfolder.

## Usage

```bash
python move_duplicates.py
```

You will be prompted to enter the folder path to scan. Any duplicate files found will be moved to a `duplicates/` folder inside that directory.

## How it works

1. Walks the target directory recursively
2. Computes an MD5 hash for each file
3. Identifies files that share a hash (i.e. identical content)
4. Moves duplicates into `<target_folder>/duplicates/`

## Requirements

Python 3 — no external dependencies.
