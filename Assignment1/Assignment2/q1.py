def calculate(a, b):
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    
    if b != 0:
        print("Quotient:", a / b)
    else:
        print("Quotient: Cannot divide by zero")


num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

calculate(num1, num2)