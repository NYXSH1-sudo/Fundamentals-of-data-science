print("Enter at least 12 numbers separated by spaces:")
user_input = input("Input: ")

# Convert input string to a list of numbers
numbers = [float(x) for x in user_input.split()]

# Validate that user entered at least 12 elements
if len(numbers) < 12:
    print(f"Error: You entered only {len(numbers)} numbers. Please enter at least 12.")
else:
    print(f"\nOriginal list ({len(numbers)} elements): {numbers}")

    # Sort the list
    numbers.sort()
    print(f"Sorted list: {numbers}")

    # Slicing operations
    print(f"\nSlice index 3 to 6   (index 3-6): {numbers[3:6]}")
    print(f"Slice index 6 to 9   (index 6-9): {numbers[6:9]}")
    print(f"Slice index 4 to 10 (index 4-10): {numbers[4:10]}")