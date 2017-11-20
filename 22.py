# What is the total of all the name scores in the file?

# Given a letter, return its position in the alphabet
# A -> 1, B -> 2, ... Z -> 26
def letter_to_position(letter):
    return ord(letter) - 64 # 64 = ord('A') - 1

# Given a name, return the sum of the positions of the letters in the alphabet
def name_to_letter_sum(name):
    letter_sum = 0
    for letter in list(name):
        letter_sum += letter_to_position(letter)
    return letter_sum

# Read in the file
with open('22input.txt') as f:
    file_contents = f.read()

# Split up the string into an array
file_contents = file_contents.split(",")

# Remove the quotes from all of the names
for i in range(len(file_contents)):
    file_contents[i] = file_contents[i][1:-1]

# Sort in alphabetical order
file_contents.sort()

sum_name_scores = 0
for i in range(len(file_contents)):
    sum_name_scores += (i+1) * name_to_letter_sum(file_contents[i])

print("Sum of name scores = " + str(sum_name_scores))
