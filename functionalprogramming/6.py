#the limit is 1000 by default for the infinite recursion(996 times printed)
#we can change the limit by importing the sys module
# import sys 
# # print(sys.getrecursionlimit()) #the limit is printed, w ecan change
# sys.setrecursionlimit(200)
# print(sys.getrecursionlimit())
# #recursion
# def rec():
#     print("hello")
#     return rec()
# rec()    

#question(print the numbers 10 from 0 by recursion)
# def natural(n):
#     if n ==0:
#         return
#     print(n, end = " ")
#     return natural(n-1)
# natural(10)

# #factorial
# factorial = 1
# def fact(n):
#     global factorial
#     if n ==0:
#         return factorial
#     factorial = factorial*n 
#     return fact(n-1)
# print(fact(3))           #nice

#factorial
#without using the global variable
# def fact(n):
#     if n ==0:
#         return 1
#     return n * fact(n-1)

# print(fact(3))     

'''
there are two types of recursive functions
1) direct ->as above; when the function calls itself directly
2) indirect -> when the function calls another function and it calls the first function
'''
# def printing(n):         #indirect recursuion
#     if n ==0:
#         return
#     print(n)
#     return printing_(n-1)
# def printing_(n):
#     if n==0:
#         return
#     print(n)
#     return printing(n-1)
# printing_(10)           #i called the printing_ function, that function calls the printing function with value 9, and it calls the first function

#fibonacci series
'''0 1 1 2 3 5 7 12 19 31....
a = 1 b = 1 series = a+b,
a = b  ->1
b = series ->2
series = a+b
this is the logic for the loop but for recursion, only a simple logic implements
# '''
# def fibo(n):
#     if n ==1:
#         return 0
#     if n ==2:
#         return 1
#     return fibo(n-2) + fibo(n-1)
# user_input = int(input("enter the number of term in fibonacci series:- "))
# print(fibo(user_input))          #it will the 10th term
# for i in range(1,user_input+1):
#     print(fibo(i)) # it wll give the no of terms that are 10

#-----------------------fibonacci program--------------------------------------------
# def fibo(n):
#     if n ==1:
#         return 0
#     if n ==2:
#         return 1
#     return fibo(n-2) + fibo(n-1)

# while True:
#     choice = int(input('''
#                     Enter 1 to execute the program A
#                     Enter 2 to execute the program B
#                     1 to find the nth term
#                     2 to find the no.of terms
#                     0 to exit!
#     enter='''))
#     if choice == 1:
#         user_input = int(input("Enter the term:- "))
#         term = fibo(user_input)
#         print(f"The {user_input} term in fibonacci series is :- {term}!!")

#     elif choice == 2:
#         user_ =int(input("Enter the No.of terms you want in fibonacci series:-"))
#         for i in range(1,user_+1):
#             print(f"The {i} term is {fibo(i)}!")
#     elif choice ==0:
#         print("Exiting!!")
#         break
#     else:
#         print("Invalid entry!!!")

'''
difference between the iteration and recursion
there are many programs we can do using both recursion and iteration like the factorial and fibonacci, for factorial there 
is indeed the same code, but for fibonaaci using iteration we have to use variables, so recursion is better,
advantages of recursion:- clean code, elegant, less code
disadvantages:- more memory, time complexity, handling infinity

*as we know during the function call, the track is stored in a stack, so recursion uses a lot of space by multiple function caling
while the iteration is not a function call, hence it don't requre the stack memory
*Time complexity for iteration is o(n) direct relation but in the recursion it is o(n), for sec call o(2**n) and so on
Infinite recursion :- Crash the system
Infinite Iteration :- Stops the application

so which is better,
It depends..
Recursive way:- Less & elegant code
Iterative way:- time & space complexity
'''
'''
LEGB --> local > enclosed/nonlocal > global > built-in
variables checking start from inner to outer
non local variables are those that are not local and global bcz they are enclosed inside the function and have a function inside too
'''
# x = 10      #global variable
# def outer():
#     x = 100 #local variable
#     print(x)
# outer()   #it will check accroding to LEGB, first in local, then non local...
          #if i comment the local variable, it wll check the global and hence 10 is printed

# x = 10      #global variable
# def outer():
#     x = 100 #non-local variable
#     print(x)
#     def inner(): 
#         # x = 1000 #local
#         print(x)
#     inner()
# outer()
#comment the variables and see how the program moves from inner to outer variables

'''
The official Python documentation defines namespace as mapping from names to objects, and scope is the textual
region of a Python program where the namespace is directly accessible. At this point, the dictionary with its
key value pairs serves as the ideal data structure for the mapping of names and objects. You have also learned 
how every Python file can be a module. You can view the same module as a place where Python creates a module object.
A module object contains the names of different attributes defined inside it. In this way, modules are a type of namespace. 
Namespaces and scopes can become very confusing very quickly and so it is important to get as much practice of scopes as 
possible to ensure a standard of quality.
Types of namespaces:
Built-in namespace
Module level/global namespace
Local namespace
Enclosed Namespace

namespaces is the container that containes the names of variables/identifiers and mapping them with their values

'''
# a = 1
# b = 2
# c = 4
# d = 5
# print(id(a), id(1))   
# print(id(b), id(2))
# print(id(c), id(4))
# print(id(d), id(5))

# all these are in one namespace, like dictionary python ensure that no duplicate key name exists
# a = 1
# a = 4 
# b = 10
# print(id(a)) #4 value is overwritten on 1 for a
# print(id(b))

#local, global, namespaces
'''
Closure is a technique by which data gets attached to the
code.
Closures are function objects that remembers values in
the enclosing scope even if they are not present in the
memory.
there are two conditions for closure:- 
There must be a nested fnction
the nested function must be returned by the parent function
'''
# def outer():
#     def inner():
#         x = 100
#         return x
#     return inner #the function is returned
# print(outer())   #gives the memory loation of inner, after this execution the python garbage collector vanishes the data, but the data is printed is due to closure, data is attached to the obj
# inner = outer()  #alias giving the value that is, is atteched to the function obj that is returned
# print(inner())

'''
functions which takes other functions as input,add
additional functionalities and returns it., as if i dont have access to the main function, we can make decorator and modifies
Function-->Decorator--> modified Function
the decorator is the callable python object which modifies another function or class
it is a high order function
two types of decorator
In this file, function decorator is explaianed, remains the class decorator
'''
# def decor(display):
#     def inner():
#         display()       #existing functionality
#         #adding new
#         print("how are you!")
#     return inner


# def display():
#     print("Hey!")
#     print("ayesha")

# display = decor(display)         #we have to display "how are you" also, so this decor function is the decoator, intead of this we can write @ and decor name
# display()                        #we dont need to print it
# def decor(display):
#     display()       
#     #adding new
#     print("how are you!")

# @decor
# def display():
#     print("Hey!")
#     print("ayesha")
    
# display()
# i am facing error in the above code, bcz of the type error bcz my decoraotor is returning nothing, instead it is calling the function, that ia invalid
#decorator retrns a function(modified)

# def decor(display):
#     def inner():
#         display()       
#         #adding new
#         print("how are you!")      #this is the cllosure concept, i am returning the
#     return inner                   #function obj

# @decor
# def display():
#     print("Hey!")
#     print("ayesha")
    
# display()

#question to modify the function that adds two number into three numbers
# def decor(add):
#     def inner():
#         result = add()
#         n3 = float(input("enter third number:- "))
#         result +=n3
#         return result
#     return inner

# def add():
#     n1 = float(input("Enter first number:- "))
#     n2 = float(input("Enter second number:- "))
#     result = n1+n2
#     return result
# add = decor(add)       #instaed of this we can write @decor above the add
# print(add())
'''
add = decor(add) replaces the original add function with the inner function returned by decor.
Now, add() refers to the inner() function within decor.
'''
#multiple decor to a function
#apply a decorator to uppercase the full name, and second decortaor to split the name
# def upp(name):
#     def inner():
#         output = name()
#         return output.upper()
#     return inner
# def spl(name):
#     def inner():
#         output = name()
#         return output.split()
#     return inner
   
# def name():
#     first_name = input("Enter your first name:- ")
#     second_name = input("Enter your second name:- ")
#     full_name = first_name + " " + second_name
#     return full_name

# name = spl(upp(name))
# print(name())                                                

# def upp(name):
#     def inner():
#         output = name()
#         return output.upper()
#     return inner
# def spl(name):
#     def inner():
#         output = name()
#         return output.split()
#     return inner
# @spl
# @upp
# def name():
#     first_name = input("Enter your first name:- ")
#     second_name = input("Enter your second name:- ")
#     full_name = first_name + " " + second_name
#     return full_name
# print(name())    

'''
applying same decorator to multiple function
we have to apply the decorator that if the second and third value is zero, it should display zero dividing error
'''
# def decor(divide):
#     def inner(*arg):
#         for n in arg[1:]:
#             if n == 0:
#                 return "divide by zero"
#         divide(*arg)
#     return inner

# @decor
# def divide1(n1, n2):
#     return n1/n2
# @decor
# def divide2(n1, n2, n3):
#     return n1/n2/n3


# print(divide2(2, 0, 5))
# print(divide2(2, 10, 5))
# print(divide1(2, 0))
# print(divide1(0, 10))

'''
smart division decorator
'''
# def divide(n1, n2):
#     print("division is ", n1/n2)

# divide(10,0)                 #it gives zerodivisonerror that will stop the program and isn't printing the print statement, we can handle it by decorator also by exception handling
#print("hello")

# def smart_division(function):
#     def inner(n1, n2):
#         if n2 == 0:
#             print("divide by zero error")
#             return
#         function(n1, n2)
#     return inner

# @smart_division  #divide = smart_division(divide)
# def divide(n1, n2):
#     print("division is", n1/n2)       

# divide(10,0)  
# print("hello")

