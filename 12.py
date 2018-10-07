# TOO SLOW

# Given a number, return the total number of factors it has
# (including 1 and itself)
def numFactors(num):
    total = 0
    for i in range(1, num+1):
        if num%i == 0:
            total += 1
    return total

triangleNumber = 1
incrementSize = 2

while True:
    triangleNumber = triangleNumber + incrementSize
    incrementSize += 1
    print(str(triangleNumber) + " has " + str(numFactors(triangleNumber)) + " factors")
    if numFactors(triangleNumber) > 500:
        break

print(triangleNumber)
