import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

#Total sum of elements
total_sum = np.sum(arr)
print(f"\na) Total sum of elements: {total_sum}")

# Mean value of the array
mean_val = np.mean(arr)
print(f"b) Mean value of the array: {mean_val}")

# Largest and smallest values
largest = np.max(arr)
smallest = np.min(arr)
print(f"c) Largest value: {largest}")
print(f"   Smallest value: {smallest}")