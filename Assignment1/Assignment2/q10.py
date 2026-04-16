import random

dice = random.randint(1, 6)

guess = int(input("Guess the dice value (1 to 6): "))

print(f"\nDice value was: {dice}")


if guess == dice:
    print(" Correct! Great guess!")
elif abs(guess - dice) == 1:
    print(" So close! You were just 1 away.")
else:
    print(" Wrong guess. Try again!")