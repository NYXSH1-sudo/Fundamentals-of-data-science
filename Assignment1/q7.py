start = 1000
end = 2500

choice = input("Do you want to enter your own range? (y/n): ")

if choice.lower() == 'y':
    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

print(f"\nNumbers between {start} and {end} divisible by 9 but not by 6:\n")

for num in range(start, end + 1):
    if num % 9 == 0 and num % 6 != 0:
        print(num)