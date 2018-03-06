import sys
import string

my_list=[[-1,"ciao"]]
for line in sys.stdin:
    for word in line.split( ):
        if word.isdigit()==True:
            # print(word)
            numbers=[x[0] for x in my_list]
            if word in numbers:
                a=numbers.index(word)
                my_list[a].append(line)
                # print("already there")
            else:
                my_list.append([word, line])
                # print("I will add an element", word, line)
            break

my_list.sort(key=lambda x: int(x[0]), reverse=True)
# print(my_list)
lines=[x[1:] for x in my_list[:-1]]
# print(lines)
a=1
for i in lines:
    for j in i:
        print(j),
    a+=1
    if a>=int(sys.argv[1]):
        exit()
