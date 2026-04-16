def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

prime_numbers = []
count = 0
total = 0

for num in range(start, end + 1):
    if is_prime(num):
        prime_numbers.append(num)
        count += 1
        total += num

print("\nPrime numbers in the given range:", prime_numbers)
print("Count of prime numbers:", count)
print("Sum of prime numbers:", total)