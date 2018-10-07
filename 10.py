# TOO SLOW

# Sum of all primes below 2,000,000

# Returns true/false depending on if a number is prime or not
def isPrime(num):
    if num == 1: # 1 is not prime
        return False
    elif num == 2: # 2 is prime
        return True
    elif num%2 == 0: # All other even numbers are not prime
        return False
    # Check if divisible by every odd number x such that: 3 <= x < num
    for i in range(3, num, 2):
        if num%i == 0:
            return False
    return True

sum = 2 # 2 is the only even prime number so add that to the sum
for i in range(1, 2000000, 2): # Now check every odd number under 2000000 to see if it is
    if isPrime(i):
        sum += i
print(sum)
