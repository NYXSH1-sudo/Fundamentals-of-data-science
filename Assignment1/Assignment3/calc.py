"""
Q3: calc_operations.py - Accepts integer lists, performs basic ops (+ sum, sub/mult/div pairwise),
saves with datetime to file; displays formatted on exit.
Author: Seshank Kumar Sharma,SEC-B.
Date: 2026-04-17
"""
import os
from datetime import datetime


def get_integers():
    '''Prompt user to enter a list of integers separated by spaces.'''
    while True:
        raw = input("Enter integers separated by spaces: ").strip()
        parts = raw.split()
        try:
            numbers = [int(p) for p in parts]
            if len(numbers) < 2:
                print("  Please enter at least 2 integers.")
                continue
            return numbers
        except ValueError:
            print("  Invalid input. Please enter whole numbers only.")


def perform_operations(numbers):
    '''Perform add, subtract, multiply, divide on the list of integers.'''
    total_add  = sum(numbers)
    total_sub  = numbers[0]
    total_mul  = numbers[0]

    for n in numbers[1:]:
        total_sub -= n
        total_mul *= n


    total_div = None
    div_error = None
    try:
        result = numbers[0]
        for n in numbers[1:]:
            if n == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= n
        total_div = round(result, 4)
    except ZeroDivisionError as e:
        div_error = str(e)

    return total_add, total_sub, total_mul, total_div, div_error


def format_result(numbers, add, sub, mul, div, div_err):
    '''Format a single result block as a string.'''
    nums_str = ", ".join(str(n) for n in numbers)
    div_str  = str(div) if div is not None else f"Error – {div_err}"

    lines = [
        f"Numbers        : {nums_str}",
        f"Addition       : {add}",
        f"Subtraction    : {sub}",
        f"Multiplication : {mul}",
        f"Division       : {div_str}",
        "-" * 20,
    ]
    return "\n".join(lines)


def display_file(filepath):
    '''Read and print the contents of the result file.'''
    print("\n" + "=" * 45)
    print(f"  Results saved in: {os.path.basename(filepath)}")
    print("=" * 45)
    with open(filepath, "r") as f:
        print(f.read())
    print("=" * 45)


def main():
    # Create a timestamped filename once per session
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename  = f"results_{timestamp}.txt"

    print("=" * 45)
    print("   Integer Arithmetic Calculator")
    print("=" * 45)
    print("Type 'exit' at any prompt to quit.\n")

    session_count = 0

    while True:
        user_in = input("\nPress Enter to continue or type 'exit' to quit: ").strip().lower()
        if user_in == "exit":
            break

        numbers = get_integers()
        add, sub, mul, div, div_err = perform_operations(numbers)
        result_block = format_result(numbers, add, sub, mul, div, div_err)

    
        with open(filename, "a") as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}]\n")
            f.write(result_block + "\n")

        session_count += 1
        print(f"\n  Result #{session_count} saved.")
        print(result_block)

    if session_count == 0:
        print("\nNo operations performed. Goodbye!")
    else:
        display_file(filename)
        print("Goodbye!")


# Main
main()