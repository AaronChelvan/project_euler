# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

current_num = 1
prev_num = 1
index = 2
while len(str(current_num)) < 1000:
    temp = current_num
    current_num = current_num + prev_num
    prev_num = temp
    index += 1

print("Index = " + str(index))
