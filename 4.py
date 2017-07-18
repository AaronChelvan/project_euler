# Find the largest palindrome which is a multiple of 2 3-digit numbers
import math

# Returns True/False depending on whether a number is a palindrome or not
def isPalindrome(num):
    num = str(num)
    for i in range(math.floor(len(num)/2)):
        if num[i] != num[len(num)-1-i]:
            return False
    return True

largestPalindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i*j) and i*j > largestPalindrome:
            largestPalindrome = i*j

print(largestPalindrome)
