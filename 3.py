# Largest prime factor of 600851475143
largestPrime = 0

# Returns true/false depending on if a number is prime or not
def isPrime(num):
    if num == 2: # 2 is prime
        return True
    elif num%2 == 0: # All other even numbers are not prime
        return False
    # Check if divisible by every odd number x such that: 3 <= x < num
    for i in range(3, num, 2):
        if num%i == 0:
            return False
    return True

for i in range(1, 600851475143):
    if 600851475143%i == 0 and isPrime(i) and i > largestPrime:
        largestPrime = i
        print("New largest prime: " + str(largestPrime))
