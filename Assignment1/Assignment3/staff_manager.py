"""
Q7: staff_manager.py - Staff class; add multiple staff, write to staff.csv, view list.
Uses try-except. Attributes: empid, fullname, address, phonenumber, maritalstatus, dependents, salary.
Author: Seshank Kumar Sharma,SEC-B.
Date: 2026-04-17
"""
import csv
import os

FILENAME   = "staff.csv"
FIELDNAMES = ["emp_id", "full_name", "address", "phone_number",
              "marital_status", "dependents", "salary"]


# ─── Staff Class ────────────

class Staff:
    '''Represents an employee with personal and payroll details.'''

    def __init__(self, emp_id, full_name, address, phone_number,
                 marital_status, dependents, salary):
        self.emp_id         = emp_id
        self.full_name      = full_name
        self.address        = address
        self.phone_number   = phone_number
        self.marital_status = marital_status
        self.dependents     = dependents
        self.salary         = salary

    def to_dict(self):
        '''Return staff attributes as a dictionary (for CSV writing).'''
        return {
            "emp_id":         self.emp_id,
            "full_name":      self.full_name,
            "address":        self.address,
            "phone_number":   self.phone_number,
            "marital_status": self.marital_status,
            "dependents":     self.dependents,
            "salary":         self.salary,
        }

    def display(self):
        '''Print staff details in a readable format.'''
        print(f"\n  {'Emp ID':<18}: {self.emp_id}")
        print(f"  {'Full Name':<18}: {self.full_name}")
        print(f"  {'Address':<18}: {self.address}")
        print(f"  {'Phone Number':<18}: {self.phone_number}")
        print(f"  {'Marital Status':<18}: {self.marital_status}")
        print(f"  {'Dependents':<18}: {self.dependents}")
        print(f"  {'Salary':<18}: Rs. {self.salary}")
        print("  " + "-" * 40)


# ─── File Helpers ────────

def ensure_file():
    '''Create staff.csv with header if it does not exist.'''
    if not os.path.exists(FILENAME):
        try:
            with open(FILENAME, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writeheader()
            print(f"  '{FILENAME}' created.\n")
        except IOError as e:
            print(f"  Error creating file: {e}")


def save_staff(staff_obj):
    '''Append a single Staff object to the CSV file.'''
    try:
        with open(FILENAME, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writerow(staff_obj.to_dict())
        print(f"\n  ✔ '{staff_obj.full_name}' saved to '{FILENAME}'.")
    except IOError as e:
        print(f"\n  ✘ Error writing to file: {e}")


def load_all_staff():
    '''Read all staff records from CSV and return a list of Staff objects.'''
    staff_list = []
    try:
        with open(FILENAME, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                s = Staff(
                    row["emp_id"], row["full_name"], row["address"],
                    row["phone_number"], row["marital_status"],
                    row["dependents"], row["salary"]
                )
                staff_list.append(s)
    except FileNotFoundError:
        print(f"  ✘ '{FILENAME}' not found.")
    except KeyError as e:
        print(f"  ✘ Missing column in CSV: {e}")
    except IOError as e:
        print(f"  ✘ Error reading file: {e}")
    return staff_list


# ─── Input Helper ────────────

def get_input(prompt, validate_numeric=False):
    while True:
        val = input(prompt).strip()
        if not val:
            print("  Field cannot be empty. Try again.")
            continue
        if validate_numeric:
            try:
                float(val)
            except ValueError:
                print("  Please enter a valid number.")
                continue
        return val


def input_staff():
    '''Collect staff details from user and return a Staff object.'''
    print("\n  --- Enter Staff Details ---")
    emp_id         = get_input("  Emp ID          : ")
    full_name      = get_input("  Full Name       : ")
    address        = get_input("  Address         : ")
    phone_number   = get_input("  Phone Number    : ")
    marital_status = get_input("  Marital Status  : ")
    dependents     = get_input("  Dependents      : ", validate_numeric=True)
    salary         = get_input("  Salary          : ", validate_numeric=True)

    return Staff(emp_id, full_name, address, phone_number,
                 marital_status, dependents, salary)


# ─── Main ────────────

def main():
    ensure_file()

    while True:
        print("\n" + "=" * 45)
        print("         STAFF MANAGEMENT SYSTEM")
        print("=" * 45)
        print("  1. Add new staff member")
        print("  2. View all staff")
        print("  3. Exit")
        print("=" * 45)

        choice = input("  Enter choice (1-3): ").strip()

        if choice == "1":
            staff = input_staff()
            save_staff(staff)

        elif choice == "2":
            staff_list = load_all_staff()
            if not staff_list:
                print("\n  No staff records found.")
            else:
                print(f"\n  === Staff List ({len(staff_list)} record(s)) ===")
                for s in staff_list:
                    s.display()

        elif choice == "3":
            print("\n  Exiting. Goodbye!")
            break

        else:
            print("  Invalid choice. Enter 1, 2, or 3.")


# Main
main()