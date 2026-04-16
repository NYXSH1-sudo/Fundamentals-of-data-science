def display_menu():
    print("\nMenu:")
    print("1. Enter a number")
    print("2. Show sums")
    print("3. Exit")


def main():
    positive_sum = 0
    negative_sum = 0

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            try:
                number = float(input("Enter a number: "))
                if number > 0:
                    positive_sum += number
                elif number < 0:
                    negative_sum += number
                else:
                    print("Zero does not affect the sums.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "2":
            print(f"\nSum of positive numbers: {positive_sum}")
            print(f"Sum of negative numbers: {negative_sum}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 3.")


if __name__ == "__main__":
    main()