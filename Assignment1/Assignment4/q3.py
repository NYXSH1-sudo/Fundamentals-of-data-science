import numpy as np # type: ignore

# Generate an array of 12 random integers between 1 and 100
random_array = np.random.randint(1, 100, size=12)
print("Original random array (1x12):")
print(random_array)

# Sort the array
sorted_array = np.sort(random_array)
print("\nSorted array:")
print(sorted_array)

# Reshape into a 3x4 matrix
matrix_3x4 = sorted_array.reshape(3, 4)
print("\nReshaped into 3x4 matrix:")
print(matrix_3x4)

# Also show 4x3 reshape
matrix_4x3 = sorted_array.reshape(4, 3)
print("\nReshaped into 4x3 matrix:")
print(matrix_4x3)

print(f"\nOriginal shape: {random_array.shape}")
print(f"3x4 matrix shape: {matrix_3x4.shape}")
print(f"4x3 matrix shape: {matrix_4x3.shape}")