# Find the sum of all multiples of 3 and 5, which are less than 1000
sum = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        sum += i

print(sum)
