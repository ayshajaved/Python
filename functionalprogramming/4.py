#lambda functions
'''
lambda aguments : python statement/expression
lambda function can't return multiple statements like in simple function it can return multiple by comma seperating
but in the form of tuple
to call, create alias for lambda
'''
# add = lambda x,y : x+y
# print(add(2, 4))

# a= lambda x,y : (x+y,x-y)
# print(a(10,4))
# add, sub = (14, 6)
# print(f"addition is {add} and subtraction is {sub}")

'''
lambda n: n+1 "incrementing lambda function"
lambda n : n**2 "power"
need:
Below are some reasons:-
The purpose of lambda functions is to be used as
parameters for functions that accept functions as
parameters.
codeno.tech
Mostly used in higher order functions.
Very useful for small expressions and Less code required.
Lambda functions are very useful when we use
filter(),map() reduce and higher order functions
'''
#sorted()
# #This function is used to sort the same type of data types
# print(sorted([2,5,1,28,99,90]))
# print(sorted(["ayesha", "amdfdfdfdfdna", "tehm", "fatima"], key = len))
#sorted according to len

#sorted() with lambda
# def func(name):
    # return name.split()[1]

# data = ["maheen fatima","ayesha javed", "muhammd ali", "amna musa"]
# print(sorted(data, key = func))
#now i want to sort it according to the second part of name
#we will use function

#By lambda
# data = ["maheen fatima","ayesha javed", "muhammd ali", "amna musa"]
# print(sorted(data, key = lambda name : name.split()[1]))

#nested lambda function
# def outer():
#     def add(x, y):
#         return x+y
#     return add        #function is returned

# a = outer()
# print(a(3,5))

# def outer():
#     add = lambda x,y : x+y
#     return add        #lambda function is returned

# a = outer()
# print(a(3,5))

# outer = lambda : lambda x,y : x+y         #nested lambda
# a =outer()
# print(a(2,4))

#lambda using if else
# max = lambda n1, n2: n1 if n1>n2 else n2
# print(max(99, 67))

'''
lambda using list comprehension
list comprehension
List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing list (or any iterable), optionally filtering items with a condition. The syntax for list comprehension is:
[expression for item in iterable if condition]
expression: The value or transformation you want to include in the new list.
item: The variable that takes the value of each element in the iterable.
iterable: The collection you are iterating over (e.g., a list, tuple, or range).
condition (optional): A filter that determines whether to include the item in the new list.
'''
# list = [2,4,7,1,4,5,7,9]
# sq = [n**2 for n in list]
# print(sq)

#with condition
# list = [34,67,34,67,98,6,23,23]
# result = [n for n in list if n%2 ==0]
# print(result)

#nested list comprehension
# list = [[2,3], [5,8], [6,8]]
# result = [n for rows in list for n in rows]
# print(result)

#printing the transpos of matrix(rows into columns and columns in rows)
# matrix =[ [2, 4, 5],
#           [4, 7 ,9],
#           [9, 1, 4]
#         ]                               #outer list comprehension
# result = [[row[i] for row in matrix] for i in range(len(matrix))]
# print(result) #inner list

#lambda and list comprehension
# list = [2,4,6,1,5,9]
# res = lambda list : [n**2 for n in list]
# print(res(list))

'''
Immediately Invoked Function Expression (IIFE)
IIFE functions(In javascript) "from javascript these are originated"
in these function when the function definition is written, the function is called at the same time passing arguments
in python we can do by the lambda function
'''
# print((lambda x,y : x+y)(4,9)) #the lambda us surrounded by paranthesis, the function call is next to it by passing arguments
z = (lambda n : n**3)(int(input("enter to get cube:- ")))
print(z)