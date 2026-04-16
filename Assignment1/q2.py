num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

addition = num1 + num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    modulus = num1 % num2
else:
    division = "Undefined (cannot divide by zero)"
    modulus = "Undefined (cannot divide by zero)"

exponentiation = num1 ** num2

print("\n--- Results ---")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
print(f"Modulus: {num1} % {num2} = {modulus}")
print(f"Exponentiation: {num1} ^ {num2} = {exponentiation}")