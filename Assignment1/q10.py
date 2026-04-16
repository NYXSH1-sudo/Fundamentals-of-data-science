import random

def play_game():
    secret_number = random.randint(1, 50)
    max_attempts = 7

    print("=" * 40)
    print("   🎯 NUMBER GUESSING GAME")
    print("=" * 40)
    print(f"I've picked a number between 1 and 50.")
    print(f"You have {max_attempts} attempts to guess it!\n")

    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt}/{max_attempts}")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                if 1 <= guess <= 50:
                    break
                print(" Please enter a number between 1 and 50.")
            except ValueError:
                print("  Invalid input. Please enter a whole number.")

        if guess == secret_number:
            print(f"\n Correct! You guessed it in {attempt} attempt(s)!")
            if attempt == 1:
                print(" Incredible — first try!")
            elif attempt <= 3:
                print(" Great job!")
            else:
                print(" Well done!")
            break
        elif guess < secret_number:
            print("📈 Too low! Try higher.\n")
        else:
            print("📉 Too high! Try lower.\n")

        if attempt == max_attempts:
            print(f"\nOut of attempts! The number was {secret_number}.")

def main():
    while True:
        play_game()
        print()
        replay = input("Play again? (yes/no): ").strip().lower()
        if replay not in ("yes", "y"):
            print("\nThanks for playing. Goodbye!")
            break
        print()

if __name__ == "__main__":
    main()