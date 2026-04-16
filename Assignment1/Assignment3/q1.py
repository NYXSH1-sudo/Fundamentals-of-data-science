import csv
import os

def read_records():
    filename = "records.csv"


    if not os.path.exists(filename):
        # Create a sample records.csv for demonstration
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["student_name", "roll_no", "program", "year", "group"])
            writer.writeheader()
            writer.writerows([
                {"student_name": "Bikkey Sharma", "roll_no": "1", "program": "CS", "year": "1", "group": "B"},
                {"student_name": "Rishi Shah", "roll_no": "2", "program": "COMPUTING", "year": "1", "group": "B"},
                {"student_name": "Siddhant Sah", "roll_no": "3", "program": "AI", "year": "1", "group": "B"},
            ])
        print(f"'{filename}' not found. A sample file has been created for demonstration.\n")

    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)

            # Print table header
            print("=" * 60)
            print(f"{'Student Name':<20} {'Roll No':<10} {'Program':<10} {'Year':<6} {'Group':<6}")
            print("=" * 60)

            count = 0
            for row in reader:
                print(f"{row['student_name']:<20} {row['roll_no']:<10} {row['program']:<10} {row['year']:<6} {row['group']:<6}")
                count += 1

            print("=" * 60)
            print(f"Total records: {count}")

    except FileNotFoundError:
        print(f"Error: '{filename}' not found.")
    except KeyError as e:
        print(f"Error: Missing expected column {e} in the CSV file.")


read_records()