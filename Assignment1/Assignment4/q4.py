import numpy as np # type: ignore

def input_matrix(name):
    '''Helper function to take matrix input from the user.'''
    print(f"\nEnter dimensions for Matrix {name}:")
    rows = int(input(f"  Number of rows: "))
    cols = int(input(f"  Number of columns: "))
    print(f"Enter elements of Matrix {name} row by row (space-separated):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"  Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Expected {cols} elements in row {i+1}, got {len(row)}.")
        matrix.append(row)
    return np.array(matrix)

try:
    # Input two matrices
    A = input_matrix("A")
    B = input_matrix("B")

    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)

    # -Addition-
    try:
        if A.shape != B.shape:
            raise ValueError(f"Addition requires same dimensions. A is {A.shape}, B is {B.shape}.")
        result_add = A + B
        print("\nMatrix Addition (A + B):")
        print(result_add)
    except ValueError as e:
        print(f"\nAddition Error: {e}")

    # -Subtraction-
    try:
        if A.shape != B.shape:
            raise ValueError(f"Subtraction requires same dimensions. A is {A.shape}, B is {B.shape}.")
        result_sub = A - B
        print("\nMatrix Subtraction (A - B):")
        print(result_sub)
    except ValueError as e:
        print(f"\nSubtraction Error: {e}")

    # -Multiplication-
    try:
        if A.shape[1] != B.shape[0]:
            raise ValueError(
                f"Multiplication requires A's columns ({A.shape[1]}) "
                f"to equal B's rows ({B.shape[0]})."
            )
        result_mul = np.dot(A, B)
        print("\nMatrix Multiplication (A x B):")
        print(result_mul)
    except ValueError as e:
        print(f"\nMultiplication Error: {e}")

except ValueError as e:
    print(f"Input Error: {e}")