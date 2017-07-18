# Find the smallest number divisible by all numbers from 1 to 20

currentNumber = 0
while True:
    currentNumber += 20 # Since the number has to be a multiple of 20,
                        # test 20, 40, 60, 80,... etc
    divisible = True

    # If a number is divisible by every number from 11 to 20,
    # then it is also divisible by every number from 1 to 20
    for i in range(11, 21):
        if currentNumber%i != 0:
            divisible = False
            break
    if divisible == False:
        continue
    else: # if divisible == True
        break

print(currentNumber)
