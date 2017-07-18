# Find the 10001st prime number

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

number = 2
whichPrime = 1

while True:
    number += 1
    if isPrime(number):
        whichPrime += 1
        print(str(number) + " is the " + str(whichPrime) + "th prime")
        if whichPrime == 10001:
            break;
