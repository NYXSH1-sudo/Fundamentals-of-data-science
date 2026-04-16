# Function to check Armstrong number
def is_armstrong(num_str):
    
    if not num_str.isdigit():
        return "Invalid input! Please enter a positive integer."

    num = int(num_str)
    n = len(num_str)

    total = 0
    for digit in num_str:
        total += int(digit) ** n

    if total == num:
        return f"{num} is an Armstrong number."
    else:
        return f"{num} is not an Armstrong number."


user_input = input("Enter a number: ")
result = is_armstrong(user_input)

print("\nResult")
print(result)