# Sum of all even numbers less than 4,000,000 in the Fibonacci sequence
currentTerm = 1
nextTerm = 2
temp = ""
sum = 0

while currentTerm < 4000000:
    if currentTerm%2 == 0:
        sum += currentTerm
    temp = nextTerm
    nextTerm = nextTerm + currentTerm
    currentTerm = temp

print(sum)
