# Import libraries

import sys
import string

# Initialize list
my_list=[[-1,"ciao"]]

# Read the lines
for line in sys.stdin:
    for word in line.split():
        # Check if it is a digit
        if word.isdigit() == True:
            numbers=[x[0] for x in my_list]
            if word in numbers:
                tmp=numbers.index(word)
                my_list[tmp].append(line)
                # print("already there")
            else:
                my_list.append([word, line])
                # print("I will add an element", word, line)
            break

# Sort the list with respect to the first element
my_list.sort(key = lambda x: int(x[0]), reverse=True)

# Revert the list
lines=[x[1:] for x in my_list[:-1]]
acc=1
for i in lines:
    for j in i:
        print(j),
    acc+=1
    if acc>=int(sys.argv[1]):
        exit()
