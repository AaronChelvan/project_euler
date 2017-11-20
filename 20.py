# The sum of the digits in the number 100!

factorial100 = 1
for i in range(1, 101):
    factorial100 = factorial100 * i

digits = list(str(factorial100))

sum_digits = 0
for i in digits:
    sum_digits += int(i)

print("Sum = " + str(sum_digits))
