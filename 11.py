# Find the largest product of 4 adjacent numbers (vertically, horizontaly, or diagonally) in a 20x20 grid of numbers

# Read in the 20x20 grid and store it as a 2D list
with open('11input.txt') as f:
    grid = f.readlines()

for i in range(20):
    grid[i] = grid[i].rstrip() # Remove the newline character
    grid[i] = grid[i].split() # Split the string by whitespace

for i in range(20):
    for j in range(20):
        grid[i][j] = int(grid[i][j]) # Convert all strings into integers

largestProduct = 0

# Scan all possible horizontal combinations of numbers
for i in range(20-4):
    for j in range(20):
        product = grid[j][i] * grid[j][i+1] * grid[j][i+2] * grid[j][i+3]
        if product > largestProduct:
            largestProduct = product

# Scan all possible vertical combinations of numbers
for i in range(20):
    for j in range(20-4):
        product = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
        if product > largestProduct:
            largestProduct = product

# Scan all possible diagonal combinations of numbers
for i in range(20-4):
    for j in range(20-4):
        product = grid[j][i] * grid[j+1][i+1] * grid[j+2][i+2] * grid[j+3][i+3]
        if product > largestProduct:
            largestProduct = product

for i in range(3, 20):
    for j in range(20-4):
        product = grid[j][i] * grid[j+1][i-1] * grid[j+2][i-2] * grid[j+3][i-3]
        if product > largestProduct:
            largestProduct = product

print(largestProduct)
