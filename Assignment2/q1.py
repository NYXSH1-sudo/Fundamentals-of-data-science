def arithmetic_operations(a: int, b: int) -> None:
    
    print(f"\n{'='*35}")
    print(f"  Results for {a} and {b}")
    print(f"{'='*35}")
    print(f"  Sum        : {a} + {b} = {a + b}")
    print(f"  Difference : {a} - {b} = {a - b}")
    print(f"  Product    : {a} × {b} = {a * b}")

    if b != 0:
        quotient = a / b
        print(f"  Quotient   : {a} ÷ {b} = {quotient:.2f}")
    else:
        print("  Quotient   : undefined (division by zero)")

    print(f"{'='*35}\n")


if __name__ == "__main__":
    arithmetic_operations(20, 4)
    arithmetic_operations(15, 3)
    arithmetic_operations(10, 0)  