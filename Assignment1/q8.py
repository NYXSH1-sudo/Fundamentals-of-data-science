def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


user_input = input("Enter a positive integer: ")

try:
    num = int(user_input)

    if num <= 0:
        print("Invalid input! Please enter a positive integer.")
    else:
        print(f"Factorial of {num} is {factorial(num)}")

except ValueError:
    print("Invalid input! Please enter a positive integer.")