'''
functions are used to enhance the code reusability and avoid redundancy
• Function is an organized block of reusable code.
• Functions can be called any number of times.
• Function contains a set of instructions which perform
specific tasks.
there are two types of functions -user defined -built in
Parameters:-
- Variables for holding actual values
- Present in function definition
Arguments:-
- Values provided at function call
parameters = formal arguments
arguments = actual arguments
'''
# def simple_interest(p, r, s):
#     print("The principle amount is ", p)
#     print("rate of interest is ", r)
#     print("NO of years is ", s)
#     si = (p*r*s)/100
#     print("simple interest is ", si)

# simple_interest(12,45,9.4)

#Variables and identifires
'''
variable is the memory location to store a particular value, while the identifire is the name used to identify a particular
object. eg: obj can be variable, function name, class name.
'''
#scope of variable
'''
scope of the variable is the region of the code where that variable can be accessed.
eg;
lines of code.....
lines of code.....
lines of code.....
x = 1
lines of code...
lines of code...
lines of code...
the scope of the variable x is the region below its declaration, it can't be accessed above as it will give error
'''

#functional programming identifiers
'''Functional programming, there are four types of identifiers.
local Identifiers
Global identifiers
Non-iocal identifiers
Built-in identifiers
'''
# 1)local variables
'''
local variables are the variables in the function, can't be accessed outside the function
hence the scope of the local variables is the function itself where they are declared
'''
# def display_name(name):
#     age = 20
#     print(f"{name} is {age} years old!")

# display_name("ayesha")
#both the name and age are the local variables
#these variables vanish as the function done its duty by the garbage collector in python(python memory manager)
 
#locals()
#locals() function can only be written at where the local variables are present in the function
#this function is used to print the dictionary of the local variables, and if we typecast it into len, we get the no of local variables
# def display_name(name):
#     age = 20
#     print(f"{name} is {age} years old!")
#     print(locals())
#     print(len(locals()))
# display_name("ayesha")
'''
if theres a function inside the display_name function, -display, then this display function is the local variable. the display_name is the globae functions
'''

# 2)Global variables
# country = "pakistan"          #gloal variable
# def age(age):
#     print(f"my age is {age}") #age is local variable
#     print("{x}".format(x = country))
#     # print(globals())
# age(20)
# print("-"*50)
# # print(globals())

#globals() function can be called at both places. Global variable can be accessed inside any function, but if there is a value it can't be changed
# num = 10
# def display():
#     print("the number is ", num)
# display()       #working

#but
# num = 10
# def display():
#     num+=5
#     print("the number is ", num)
# display()         #unboundlocal error, bcz the num is treated as the local variable we have to told it that it is a global

# num = 10
# def display():
#     global num
#     num+=5
#     print("the number is", num)
# display()    
# print("the num is {}".format(num))
#num is changed. as globally, so outside the function it is changed


