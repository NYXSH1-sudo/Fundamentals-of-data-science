"""
Q4: copy_files.py - Copies content from input file to output file (user-specified).
Handles exceptions.
Author: Seshank Kumar Sharma,SEC-B.
Date: 2026-04-17
"""
import os


def get_filename(prompt):
    '''Get a non-empty filename from the user.'''
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("  Filename cannot be empty. Please try again.")


def copy_file(src, dst):
    '''Copy contents of src to dst with exception handling.'''

   
    if not os.path.exists(src):
        raise FileNotFoundError(f"Input file '{src}' does not exist.")

   
    if os.path.exists(dst):
        raise FileExistsError(f"Output file '{dst}' already exists. Choose a different name.")

    # Perform the copy
    with open(src, "r") as infile:
        content = infile.read()

    with open(dst, "w") as outfile:
        outfile.write(content)

    return len(content)


def main():
    print("=" * 30)
    print("        File Copy Utility")
    print("=" * 30)

    src = get_filename("Enter the INPUT  file name : ")
    dst = get_filename("Enter the OUTPUT file name : ")

    try:
        bytes_copied = copy_file(src, dst)
        print(f"\n  Successfully copied '{src}' → '{dst}'.")
        print(f"   Characters copied: {bytes_copied}")

    except FileNotFoundError as e:
        print(f"\n  Error: {e}")

    except FileExistsError as e:
        print(f"\n  Error: {e}")

    except PermissionError:
        print(f"\n  Error: Permission denied. Check file/folder permissions.")

    except Exception as e:
        print(f"\n  Unexpected error: {e}")



main()