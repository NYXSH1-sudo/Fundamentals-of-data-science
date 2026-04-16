import math

num = float(input("Enter a number: "))

# Calculations
cube = num ** 3
cube_root = num ** (1/3)

if num > 0:
    natural_log = math.log(num)
    log_base2 = math.log2(num)
else:
    natural_log = "Undefined (log only for positive numbers)"
    log_base2 = "Undefined (log only for positive numbers)"

power_6 = num ** 6

print("\nResults:")
print("Cube:", cube)
print("Cube Root:", cube_root)
print("Natural Logarithm:", natural_log)
print("Base-2 Logarithm:", log_base2)
print("Number raised to power 6:", power_6)