def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero not allowed."
    return a / b

def floor_divide(a, b):
    if b == 0:
        return "Error! Division by zero not allowed."
    return a // b

def power(a, b):
    return a ** b

print("=== Mathematical Operations Program ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n=== Results ===")
print("Addition:", add(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Floor Division:", floor_divide(num1, num2))
print("Exponentiation:", power(num1, num2))