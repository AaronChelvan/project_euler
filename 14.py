# Find which number under 1,000,000 produces the longest Collatz sequence

# Given a number, return the length of the Collatz chain for that number
def collatzChainLength(number):
    length = 1
    while number != 1:
        if number%2 == 0:
            number = number/2
        else:
            number = number*3 + 1
        length += 1
    return length

longestChainLength = 0 # Length of the longest chain found so far
longestChainLengthNum = 0 # The number with the longest chain so far

for i in range(1, 1000000):
    chainLength = collatzChainLength(i)
    if chainLength > longestChainLength:
        longestChainLength = chainLength
        longestChainLengthNum = i

print(longestChainLengthNum)
