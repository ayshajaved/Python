# lists are more likely arrays but store different type of data
'''
In python, list is implemented as dynamic
array
In other languages like JAVA, C++ we have
static and dynamic arrays both
'''
# marks = [12, 23, 21, 89, 67]
#another way to initialize the list as constructor
# mark = list((12, 23, 21, 89, 67)) 
# print(marks, mark)
# print(marks[2])
# marks[0] = 23
# print(marks)
# print(len(marks))

# list_my = [2,5,4,3,2]
# print(*list_my)      #prints the list elements
# print(list_my)       #in list form

#list slicing
# marks = [12, 34, 55, 44, 67, 65]
# print(marks[2:4])

#list methods/functions
#name = ["ayesha", "ali", "amna", "tehreem", "abdullah"]
# print(name.append("aa"))
# print(name)
# name.insert(1,"bb")
# print(name)
# name.reverse()
# print(name)
# name.remove("ali")
# print(name)
# print(type(name))      #type of [] is list

#tuple
# tup = (1,23,45,56)      #same as list the tuple can be initialized by constructor
# print(type(tup))

#practiseq
# mov1 = input("enter the first movie name :")
# mov2 = input("enter the second movie name :")
# mov3 = input("enter the third movie name :")

# listofmovie = [mov1, mov2, mov3]
# print(listofmovie)
# print(type(listofmovie))

#another way
# mov1 = input("enter the first movie name :")
# mov2 = input("enter the second movie name :")
# mov3 = input("enter the third movie name :")

# movie = []
# movie.append(mov1)
# movie.append(mov2)
# movie.append(mov3)
# print(movie)
#also by one variable
# movie = []
# mov = input("enter the first movie name :")
# movie.append(mov)
# mov = input("enter the second movie name :")
# movie.append(mov)
# mov = input("enter the third movie name :")
# movie.append(mov)
# print(movie)

#simplest wy

# movie = []
# movie.append(input("enter first"))
# movie.append(input("enter sec"))
# movie.append(input("enter th"))
# print(movie)

#extend method
list = [23, 45, 67, "ayesha"]
n = [23, 56]
list.append(n) #it will as it is
print(list)

list.extend(n) #it will extend the n
print(list)
#list comprehension
# list= []
# for n in range(0,101):
#     list.append(n)
# print(list)
'''List comprehension is an elegant way to define and create lists based on existing lists.
List comprehension is generally more compact and faster than normal functions and I
creating list.
Syntax of List Comprehension
[expression for item in list]'''

# n = [var for var in range(0, 101)]     #in just two lines
# print(n)

#we can also filter
# n = [var for var in range(0, 101) if var%2 ==0]     #in just two line
# print(n)

# string = "ayesha"
# m = [var for var in string]              #each character in list is stored
# print(m)

#iterate over 2+ list using zip function
# l1= [22, 90, 78]
# l2=[21, 54, 76, 45]
# for a,b in zip(l1, l2):
#     print(a, b)          #it doesnt print the last element of the list2

# #we can also print it using for
# for a in range(len(l1)):
#     print(l1[a], l2[a])

#practise
#write a program to check the palindrome of elements that whether they are repeating at mid or not
# list = [1, 9, 3, 2, 1]
# listcopy = list.copy()
# listcopy.reverse()
# if(listcopy==list):
#     print("palindrome")
# else:
#     print("no")

#count the a grade in a tuple
# st = ('a','b','c','a')
# print(st.count('a'))


# values = [2, 3, 5, 1, 4, 45, 22]
# values.sort()
# print(values)
# values[2] = "23"
# print(values[2])
# print(values)
# print(values)
# values.pop(3) #if i print this then value at 3 will be printed
# print(values)

# print(values.append("ayesha")) #it returns none
# values.append("ayesha")
# print(values)
# print(values.insert(3,"23"))#returning none
# print(values)

# list copying can be a bit tricky SHALLOW COPY
# list1 = [12, 'ayesha', "amna", 3.4]
# list2 = list1
# print(list1, id(list1))     #same address and changes are applied to both
# print(list2, id(list2))
# # but if i change in a one list, the both lists get changed
# list1[2]= "tehreem"
# print(list1)
# print(list2)

# so we should use .copy method DEEP COPY
# list2 = list1.copy()
# print(list1, id(list1)) #addresses are also different
# print(list2, id(list2))
# list2[2]= "ali"
# print(list1)
# print(list2)
# #nice
'''
Deep copy can also be done usin copy library and importing deepcopy
'''
# from copy import deepcopy
# l1 = [2, 3, 5 , "ayesha"]
# l2 = deepcopy(l1)
# print(l1, l2)
# l1[3] = "ali"
# print(l1, l2, id(l1), id (l2))
# list = [23, 34, 76, "ayesha"]
# for n in list:
#     print(n)
# print("")
# for n in range(0,len(list)):
#     print(list[n])
# print("")
# for n in range(len(list)-1, 0-1, -1):
#     print(list[n])

#stack and queue
'''The stack is a linear data structure.
Stores items in a Last-ln/First-Out (LIFO) or First-ln/Last-Out (FILO) manner.
Stack Operations.
Push 1nserting an Elements
Pop  DeletionAn Element (Last Element)
Peek DispIay the Last Element
display display the list
'''

#short hand if else
# a = 23
# b = 34
# print("a>b") if a>b else print("b>a")