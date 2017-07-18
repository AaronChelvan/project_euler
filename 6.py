# The difference between the square of the sum of the first 100 natural numbers ((1 + 2 + ... + 100)^2)
# and the sum of the squares of the first 100 natural numbers (1^2 + 2^2 + ... + 100^2)

sumOfSquares = 0
for i in range(1, 101):
    sumOfSquares += i**2

squareOfSum = 0
for i in range(1, 101):
    squareOfSum += i
squareOfSum = squareOfSum**2

print(squareOfSum - sumOfSquares)
