'''
First class objects in programming:-
They are instance of some class.
Can be stored in data structures.
Can be assigned to variables.
Can perform operations on these objects.
Can be passed as arguments to functions
Can be returned as values from functions
eg: strings, function
'''
#function passing as an argument
# def name():
#     first_name =input("enter your first name:-")
#     last_name = input("enter the last name:-")
#     return first_name+ " "+ last_name
# def display(name):
#     print(name())
# display(name)        #the name function as it is passed, if i write the brackets then the value of name is passes, error

'''
A function is called as higher order functions if
o It contains other functions as parameters
OR
o Returns a function as an output for further processing.

'''
# def add(n,m):
#     print(n+m)
# def show(func): # show is an higher order function
#     func(4,8)
# show(add)

#some higher order functions
'''
filer() map() reduce()
many higher order functions are in the module functools
'''
'''
filter function takes two mandatory arguments, 1-function(condition for filtering) 2-data to be filtered
it returns the iterator of the filtered obj, if we print the filtered obj, it prints memory, to print the values
use for loop or convert into list
the filtered obj are the only values that are true and false values are neglected
Important point:- the filtered objects can only be acessible once
'''
# data = [2,9,5,3,2,11,98]
# def even(num):
#     if num%2 ==0:
#         return True
#     else:
#         return False
    

# filtered_bj = filter(even,data)   #the even function is checked for each value of the data
# print(filtered_bj) #the location of filtered objects

# for i in filtered_bj:     
#     print(i)
# print(list(filtered_bj))  #if the above statement is executed along with the this,retrns nothing

#we can also use the lambda funtion

# data = [2,5,56,3,2,5,6,65]
# filtered_obj = filter(lambda n: n%2,data)
# print(list(filtered_obj))

#Question filter vowels from the string
# string = "ayeshajaved"
# def vowels(n):
#     if n == "a" or n =="e" or n =="i" or n =="o" or n =="u": #it worked
#         return True
#     else:
#         return False
# filtered_obj = filter(vowels, string)
# print(list(filtered_obj))

# string = "ayeshajaved"
# def vowels(n):
#     if n in "aeiou":
#         return True
#     else:
#         return False
# filtered_obj = filter(vowels, string)
# print(list(filtered_obj))

# string = "ayeshajaved"
# def vowels(n):
#     return n in "aeiou"
# filtered_obj = filter(vowels, string)
# print(list(filtered_obj))

#question
#filter students having marks greater to or equal to 90
# dict = {
#     "ayesha" : 99,
#     "amna"   : 89,
#     "ali"    :92,
#     "fatima" :76,
#     "tehreem": 90
# }
# def marks(n):
#     if dict[n] >= 90:
#         return True
#     else:
#         return False
# filtered_obj = filter(marks,dict)
# print(list(filtered_obj))

'''
map function
map function is the same as filter obj, it takes two arguments, function and iterable, and returns the function output
'''
# names = ["ayesha","amna", "tehreem", "fatima"]
# def counting_len(name):
#     return name, len(name)
# mapped_objects = map(counting_len, names)
# # print(list(mapped_objects))           #mapped objects can only be used once
# for i in mapped_objects:
#     print(i[1])

# list1 = [2,3,4,5,6,7]
# def sq(n):
#     if n%2!=0: #odd
#         return n**2
#     else:
#         return n      #there is no concept of True or false here. the value is returned whether zero or non zero
    
# mapped_obj = map(sq, list1)
# print(mapped_obj)
# print(list(mapped_obj))

#questions
#add the two lists or three
# list1 = [2,4,5,7,1,2,5]
# list2 = [3,6,7,8,9,0,2]
# list3 = [2,3]
# #we will use the map functin
# def add(n1,n2,n3):
#     return n1+n2+n3
# mapped_obj = map(add, list1,list2,list3)
# print(list(mapped_obj))                #only two outputs as the remaining elements of list2, list1 dont not have a map for them

#take user input and give them the laptops that are below their budget
# user_input = float(input("Enter your budget:- "))
# laptops = {
#     "dell" : 90000,
#     "asus" : 80000,
#     "hp"   : 65000,
#     "lenovo":100000
# }
# def lap(val):
#     if laptops[val] <= user_input:
#         return laptops.items
#     else:
#         return False


# filtered_obj = filter(lap,laptops)
# print(list(filtered_obj))

'''
reduce function unlike the filter and map functions, doesn't return an iterable but a single value that is reduced
it takes two arguments like the filter and map, the functio and the iterator, but it takes two values from the iterator and
performs function, we have to import the functools module
'''
# from functools import reduce
# list1 = [2, 4, 7, 8, 3, 4]
# def sum(a, b):
#     return a+b
# print(reduce(sum, list1))

# #by lambda
# list1 = [2, 4, 7, 8, 3, 4]
# print(reduce(lambda a,b:a+b, list1))
#mx number in the list
# list1 = [334, 543 , 32, 5 , 6678, 435, 43, 234]
# def max(a, b):
#     if a >b:
#         return a
#     else:
#         return b
# print(reduce(max, list1))

'''
Partial functions allow us to fix a certain
number of arguments of a function and
generate a new function.
'''
# from functools import partial
# def sum(n1, n2, n3, n4):
#     return n1+n2+n3+n4
# sum = partial(sum,4,7)    #n1 and n2 values are fixed by the positional arguments
# print(sum(3,5))
# print(sum(1,2))           #passing positional arguments of n3, n4

# from functools import partial
# def sum(n1, n2, n3, n4):
#     return n1+n2+n3+n4
# sum = partial(sum,n3 =4,n4 = 7)    #n3 and n4 values are fixed by the keyword arguments
# print(sum(3,5))
# print(sum(1,2))           #passing positional arguments of n1, n2
#we cannot fix the preliminary arguments as keyword, like n1, n2 in above situation, if we fix then we have to pass the keyword argumnets of n3 and n4

'''
The zip function in Python is used to combine two or more iterables (like lists, tuples, etc.) element-wise
into a single iterator of tuples. Each tuple contains the elements from the input iterables at the same position.

Unequal Lengths: If the input iterables have different lengths, zip will stop creating tuples when the shortest 
iterable is exhausted. The remaining elements in the longer iterables are not included in the result.
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print(list(zipped))

Unzipping: You can also unzip a list of tuples using zip(*zipped).
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # Output: (1, 2, 3)
print(letters)  # Output: ('a', 'b', 'c')
'''
