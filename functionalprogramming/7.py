'''
Symbol table:- It is a data structure which contains all
necessary information about global scope of the
program.
This symbol table is accessed using globals() function.• globals() function returns a dictionary of current global
symbol table.
Syntax:- globals()
we can also change the global variable directly and access
also we can access the local variable by locals() and change it but indirectly
'''
# x = 1000
# def display():
#     age = 20
#     print(f"my age is {age}")
    
# print(globals()) #in output we can see the builtin functions and the gloal variable x and the function display, we can call globals inside the fuction

# x = 1000
# def display():
#     age = 20
#     print(f"my age is {age}")    
    
#     print(globals()["x"])
#     globals()["x"]= 10
#     print(globals()["x"])
#                           #X IS CHANGED
# display()

#locals()
# x = 1000
# def display():
#     age = 20
#     print(f"my age is {age}")    
#     print(locals())     #we can also access
#     print(locals()["age"])
#     locals()["age"] = 30            #the local variable is not chnaged, to chnage we have to chnage age
#     print(locals()["age"])

# display()

'''
The difference between modifying global and local variables using globals() and locals() is rooted in how Python handles these namespaces.
Global Variables (globals()):
The globals() function returns a reference to the global symbol table (i.e., the dictionary containing all global variables).
Modifying this dictionary directly changes the actual global variables because the dictionary returned by globals() is a live view of the global symbol table.
Local Variables (locals()):
The locals() function returns a snapshot of the local symbol table (i.e., the dictionary containing all local variables within the current function or scope).
Modifying this dictionary does not affect the actual local variables. This is because locals() provides a copy of the local variables rather than a reference to the underlying local namespace.
In this case, locals()["age"] = 30 does not actually change the variable age. The dictionary returned by locals() is a copy, and changing it does not affect the actual local variables in the current scope.
Why This Difference?
Optimization and Scope Management: Python optimizes local variable access using an internal mechanism that doesn't directly map changes from the locals() dictionary back to the actual local variables. This is partly for performance reasons and to maintain consistency and scope integrity.
Globals are More Accessible: Global variables are accessible from anywhere in the code, so Python provides a direct way to modify them via the globals() dictionary. This direct access is not mirrored for local variables to prevent accidental changes to local state, which could lead to hard-to-debug issues.
'''
# x = 1000
# def display():
#     age = 20
#     print(f"my age is {age}")    
#     print(locals())     #we can also access
#     print(locals()["age"])
#     age = 30          
#     print(f"my new age is {locals()["age"]}")

# display()

'''
callable()Syntax:-
callable( python_object )
True :- If passed object is callable. otherwise false
What are callable objects?
Objects which can be called whenever required.
Objects having __call__( ) method in their class.
# '''
# x = 100
# def display():
#     print("hello")

# print(callable(x))   #false bcz the class of integers dont have __call__() method
# print(callable(display)) #function are the class that have the __call__()method
# display()                # we can call function as below
# display.__call__()       #this is the display of the __call__() method in the function class that is defined to call

#checking whether a class is callable
from typing import Any


# class ayesha:
#     def __init__(self, age):
#         self.age = age
#         print("Hello i am ayesha!")
#     def display(self):
#         print(f"My age is {self.age}")
#     def __call__(self, *arg):
#         print()
# obj = ayesha(20)
# obj.display()
# print(callable(ayesha))   #it is callable
# print(callable(obj))      #it is not callable, bcz in its class, __call__ ()method is not defined
# #to make it callable define functon of __call__()
# obj.__call__(3,6) #obj is the object of the class function that is callable, we can rename it to add in order to add

#making the __call__ method open to add multiple positional arguments
# class maths:
#     def __call__(self, *args):
#         return sum(args)
    
# add = maths()
# print(add(2,4,5,6))

'''-----------------------------------------------------------------------------------
'''
# class maths():
#     def __call__(self,operation,*args):
#         if not args:
#             print("No numbers entered!!")
#         elif operation == "add":
#             return sum(args)
#         elif operation=="substract":
#             sub = args[0]
#             for n in args[1:]:
#                 sub-=n
#             return sub
#         elif operation=="multiply":
#             result = 1
#             for n in args[0:]:
#                 result*=n
#             return result
#         elif operation == "divide":
#             res = args[0]
#             for n in args[1:]:
#                 if n == 0:
#                     return "zero divide error"
#                 res /= n
#             return res
#         elif not operation:
#             print("No operation is entered!")

# maths_operation = maths()
# print(maths_operation("add", 3, 7, 8 ,3))
# print(maths_operation("substract", 3, 7, 8))
# print(maths_operation("multiply", 3, 1, 4 ,3, 5))
# print(maths_operation("divide", 10, 0, 8 ,3))
# print(maths_operation(0, 7, 8 ,3))
# print(maths_operation("add"))

'''
class decorator
'''
# class Smart_Division():
#     def __init__(self, function):
#         self.function = function
#     def __call__(self, a,b): 
#         if b == 0:
#             print("divide by zero error")
#             return
#         self.function(a,b)

# def divide(n1, n2):
#     print("division is", n1/n2)

# divide = Smart_Division(divide) #instead of this we can write @decoratorname above the function
# divide(10, 5)

# class Sq():
#     def __init__(self, function):
#         self.function = function
#     def __call__(self, a, b):
#         res = self.function(a,b)
#         return res**2

# def product(a, b):
#     result = a*b
#     return result
# product = Sq(product)
# print(product(2,3))

#the sum of 3 numbers is done by the function, we have to decorate it in a way that if the string is entered, the error should be printed
# class Decorator():
#     def __init__(self, function):
#         self.function = function
#     def __call__(self, *args):
#         try:

#             if any([isinstance(i, str) for i in args]):
#                 raise TypeError ("Cannot pass strings!")
#             else:
#                 return (self.function(*args))
#         except Exception as obj:
#             return obj

# @Decorator
# def add(*args):
#     return sum(args)

# print(add(5,"2",3))