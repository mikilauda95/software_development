#TODO: just save what blocks you inserted at which position., then let it print it
import sys
import re
# import numpy
from operator import add


def put(obj,hole,my_map):
    ok=0
    mapped_obj=[]
    offset=obj[1][0][0]
    # print("offset")
    # print( offset )
    # print("object")
    # print(obj)
    shift_hole=[(hole[0]-offset),hole[1]]
    # print(shift_hole)
    # mapped_obj=( list(numpy.add(shift_hole ,obj[1])))
    for line in obj[1]:
        tmp_map_obj=tuple(map(add, shift_hole, line))
        # print("tmp_map")
        # print ( tmp_map_obj )
        mapped_obj.append(tuple(tmp_map_obj))

    # print("HERE IS MAPPED OBJ")
    # print(mapped_obj)
    if (set(mapped_obj) <= set(my_map)):
        # print("We can fit this")
        newmap=list(set(my_map)-set(mapped_obj))
        # print("new map")
        # print ( newmap , len(newmap))
        # print("old map")
        # print ( my_map, len(my_map) )
        returns=[newmap,mapped_obj]
        return returns

    else:
        # print("we cannot fit this :(")
        # print("old map")
        # print ( my_map, len(my_map) )
        return -1



def trytofit(obj_list,element,my_map, place_list, side):
    obj=obj_list[element]
    # print("object num", element)
    # print(obj[0])
    for hole in my_map:
        returns=put(obj,hole,my_map)
        if returns!=-1: # return True if it fits, else False. TODO Should I modify my_map?
            newmap=returns[0]
            newelement=element+1
            new_place=place_list
            new_place.append([obj[0], returns[1]])
            # print("element value is:", newelement)
            if newelement<7:
                trytofit(obj_list,newelement,newmap, new_place, side)
            if newelement==7:
                # print("completed")
                # print("FINAL PLACEMENT IS")
                final_place=[]
                for letter in [x[0][0] for x in obj_list[::-1]]:
                    # print(letter)
                    for place_elem in place_list[::-1]:
                        # print(place_elem)
                        if (place_elem[0][0])==letter:
                            # print("CIAO")
                            # print(str(place_elem[0]))
                            final_place.append(place_elem)
                            break

                # print(place_list)
                # print(final_place)
                printmap(final_place,side)


def printmap(placement,side):
    configuration=[]
    for i in range(0,side):
        configuration.append([" "]*side+["\n"])

    for obj in placement:
        for letter in obj[1]:
            # print(letter[0])
            configuration[letter[1]][letter[0]]=obj[0][0]

    string=""
    for i in configuration:
        for letter in i:
            string+=letter
    print(string),

def init_func(arg1, obj_list, init_map):

    """READ files from given as arguments and put them into a list
    :returns: TODO

    """
    #each object is put into a list with a[0] a list with information and a[1] a list of strings (each string a line)
    count=0
    for files in arg1:
        curr_file=open(files,"r")
        line_index=0
        tmp_list=[]
        for line in curr_file.read().split('\n'):
            if line!="":
                indexes=[[i.start(),line_index] for i in re.finditer('[A-Z]', line)]
                count+=len(indexes)

                tmp_list+=indexes
                # end=re.search("[A-Z]+", line).end()
                line_index+=1
        tmp_list=[[files],tmp_list]
        obj_list.append(tmp_list)
    side=int( count**(0.5))#compute how long should be a side of the square
    # print ( side )
    for i in range(0,side):
        for j in range(0,side):
            init_map.append((j,i))

    # print(init_map)




#MAIN FUNCTION

obj_list=[]
init_map=[]
newmap=[]
first_map=[]
# print(sys.argv[1:])
init_func(sys.argv[1:],obj_list,init_map)
# print ( init_map )
# print( obj_list )

#Let's try an insert
obj=obj_list[0]
side=int( len(init_map)**0.5 )
# print("ciao")

#new way of doing it: save the elements in a list of list: a list containing:character, offset and a list of coordinates. Then to check if it can be fit you just try element per element to insert them
# trytofit(obj_list,0,init_map)

#debugging if (put(obj_list[0],(0,0),init_map,first_map))!=False:

# first_map=put(obj_list[0],(0,0),init_map)
# print(first_map)
# second_map=put(obj_list[1],(3,0),first_map)
# print (second_map)
place=[]
trytofit(obj_list,0,init_map,place, side)



