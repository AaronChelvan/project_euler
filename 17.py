# Count the number of letters used if all numbers from 1 to 1000 inclusive were written out in words

# Converts a 1-digit number to a string
def num1DigitToString(num):
    if num == "1":
        return "one"
    elif num == "2":
        return "two"
    elif num == "3":
        return "three"
    elif num == "4":
        return "four"
    elif num == "5":
        return "five"
    elif num == "6":
        return "six"
    elif num == "7":
        return "seven"
    elif num == "8":
        return "eight"
    elif num == "9":
        return "nine"

# Converts a 2-digit number to a string
def num2DigitToString(num):
    if num == "10":
        return "ten"
    elif num == "11":
        return "eleven"
    elif num == "12":
        return "twelve"
    elif num == "13":
        return "thirteen"
    elif num == "14":
        return "fourteen"
    elif num == "15":
        return "fifteen"
    elif num == "16":
        return "sixteen"
    elif num == "17":
        return "seventeen"
    elif num == "18":
        return "eighteen"
    elif num == "19":
        return "nineteen"
    elif num == "20":
        return "twenty"
    elif num[0] == "2":
        return "twenty-" + num1DigitToString(num[1])
    elif num == "30":
        return "thirty"
    elif num[0] == "3":
        return "thirty-" + num1DigitToString(num[1])
    elif num == "40":
        return "forty"
    elif num[0] == "4":
        return "forty-" + num1DigitToString(num[1])
    elif num == "50":
        return "fifty"
    elif num[0] == "5":
        return "fifty-" + num1DigitToString(num[1])
    elif num == "60":
        return "sixty"
    elif num[0] == "6":
        return "sixty-" + num1DigitToString(num[1])
    elif num == "70":
        return "seventy"
    elif num[0] == "7":
        return "seventy-" + num1DigitToString(num[1])
    elif num == "80":
        return "eighty"
    elif num[0] == "8":
        return "eighty-" + num1DigitToString(num[1])
    elif num == "90":
        return "ninety"
    elif num[0] == "9":
        return "ninety-" + num1DigitToString(num[1])

# Converts a 3-digit number to a string
def num3DigitToString(num):
    if num[1] == "0" and num[2] == "0":
        return num1DigitToString(num[0]) + " hundred"
    elif num[1] == "0":
        return num1DigitToString(num[0]) + " hundred and " + num1DigitToString(num[2])
    else:
        return num1DigitToString(num[0]) + " hundred and " + num2DigitToString(num[1:3])

# Converts number from 1 to 1000 inclusive, to a string
def numToString(num):
    if len(num) == 1:
        return num1DigitToString(num)
    elif len(num) == 2:
        return num2DigitToString(num)
    elif len(num) == 3:
        return num3DigitToString(num)
    else:
        return "one thousand"

# Removes all spaces and hyphens from a string
def removeSpacesHyphens(string):
    string = string.replace(" ", "")
    string = string.replace("-", "")
    return string

# Count the total number of letters
numLetters = 0

for i in range(1, 1001):
    i = str(i)
    numLetters += len(removeSpacesHyphens(numToString(i)))
    print(numToString(i))

print(numLetters)
