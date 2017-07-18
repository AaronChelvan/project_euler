# Find the sum of the digits of 2^1000

number = str(2**1000) # Save 2^1000 as a string
number = list(number) # Convert the string into a list of characters

total = 0
for i in range(len(number)):
    total += int(number[i])

print(total)
