"""
Q5: learner_class.py - Learner class for student details; inputs and displays object.
Attributes: rollno, fullname, address, enrollmentyear, program, sec.
Author: Seshank Kumar Sharma,SEC-B.
Date: 2026-04-17
"""
class Learner:
    '''Represents a student/learner with their academic details.'''

    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        self.roll_no          = roll_no
        self.full_name        = full_name
        self.address          = address
        self.enrollment_year  = enrollment_year
        self.program          = program
        self.group            = group

    def display(self):
        '''Display learner details in a formatted table.'''
        print("\n" + "=" * 45)
        print("         LEARNER DETAILS")
        print("=" * 45)
        print(f"  {'Roll No':<18}: {self.roll_no}")
        print(f"  {'Full Name':<18}: {self.full_name}")
        print(f"  {'Address':<18}: {self.address}")
        print(f"  {'Enrollment Year':<18}: {self.enrollment_year}")
        print(f"  {'Program':<18}: {self.program}")
        print(f"  {'Group':<18}: {self.group}")
        print("=" * 45)


def get_input(prompt):
    '''Get non-empty input from user.'''
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  This field cannot be empty. Please try again.")


def main():
    print("=" * 45)
    print("   Enter Learner Information")
    print("=" * 45)

    roll_no         = get_input("Roll No          : ")
    full_name       = get_input("Full Name        : ")
    address         = get_input("Address          : ")
    enrollment_year = get_input("Enrollment Year  : ")
    program         = get_input("Program          : ")
    group           = get_input("Group            : ")


    learner = Learner(roll_no, full_name, address, enrollment_year, program, group)

  
    learner.display()



main()