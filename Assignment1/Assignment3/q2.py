'''
This program takes user details as input and appends them to the existing
file "records.csv". The fields are: student_name, roll_no, program, year, and group.
'''

import csv
import os

FILENAME = "records.csv"
FIELDNAMES = ["student_name", "roll_no", "program", "year", "group"]


def ensure_file_exists():
    '''Create records.csv with header if it does not exist.'''
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        print(f"'{FILENAME}' not found. A new file has been created.\n")


def get_input(prompt, allow_empty=False):
    '''Helper to get non-empty input from user.'''
    while True:
        value = input(prompt).strip()
        if value or allow_empty:
            return value
        print("  Input cannot be empty. Please try again.")


def append_record():
    '''Collect student details from user and append to CSV.'''
    print("\n--- Enter Student Details ---")
    student_name = get_input("Student Name : ")
    roll_no      = get_input("Roll No      : ")
    program      = get_input("Program      : ")
    year         = get_input("Year         : ")
    group        = get_input("Group        : ")

    record = {
        "student_name": student_name,
        "roll_no":      roll_no,
        "program":      program,
        "year":         year,
        "group":        group,
    }

    with open(FILENAME, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(record)

    print(f"\n✔  Record for '{student_name}' has been added to '{FILENAME}'.")


def main():
    ensure_file_exists()

    while True:
        append_record()
        another = input("\nAdd another record? (yes/no): ").strip().lower()
        if another not in ("yes", "y"):
            break

    print("\nDone. Exiting program.")


# Main
main()