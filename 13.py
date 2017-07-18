# Find the first 10 digits of the sum of the 100 50-digit numbers provided

with open('13input.txt') as f:
    numbers = f.readlines()

for i in range(100):
    numbers[i] = numbers[i].rstrip() # Remove the newline characters
    numbers[i] = int(numbers[i]) # Convert from a string to an integer

totalSum = 0
for i in range(100):
    totalSum += numbers[i]

result = str(totalSum)[0:10] # We only want the first 10 digits of the number
print(result)
