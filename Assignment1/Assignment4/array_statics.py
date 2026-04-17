"""
Q1: array_statistics.py - Creates NumPy array and computes sum, mean, max, min.
Fields: array=[10,20,30,40,50], sum, mean, max_value, min_value.
Author: Seshank Kumar Sharma, SEC-B.
Date: 2026-04-17
"""
import numpy as np # type: ignore

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