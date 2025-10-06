def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find primes between 25 and 50
for num in range(25, 51):
    if is_prime(num):
        print(num)
