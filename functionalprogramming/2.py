#return
'''
after return statement, no statement is executed
we can return multiple values by comma seperating and they will be return as tuple
Then we can assigne the values of the tuple to the differnet variables by comma seperating
default return type is none
'''
# def math(a, b):
#     sum = a+b
#     sub = a-b
#     return sum,sub
#     print("this statement won't execute!")
# result1, result2 = math(10, 2)
# print(result1,"\n",result2)   
# print(type(math))  #obj of class function

#creating multiple alias for functions
# def math(a, b):
#     sum = a+b
#     sub = a-b
#     return sum
# result = math(10, 2)
# print(result)   
# x = math
# print(x(3,2))

#nested functions
'''
the function inside the main function's scope is the outer function after function definition
it provides the privacy
the decorators are dependent on this concept
it provide the encapsulation
'''
# def display():
#     print("hello")
#     def bye():
#         print("Bye")
#     bye()           #inner function is called inside the outer function

 
# display()
# #inner function can't be called outside the main function

'''
Types of arguments:-
1. Positional arguments
2. Keyword arguments
3. Default arguments
4. Variable length arguments
'''
#positional
'''
positional arguments:-
The order in which you pass the values during the
function call should match the order in which the
parameters are defined in the function.
Number of parameters = N+ber of arguments
'''
# def info(name, age):
#     print("Name is {name}, Age is {age}".format(name = name, age = age))

# info(20, "ayesha")     #name and age reversed, function output changes

#keyword arguments
# def info(name, age):
#     print("Name is {name}, Age is {age}".format(name = name, age = age))

# info(age = 20,name =  "ayesha")   
#now the output is correct, order is not important
#if we don't know the definition we can use the keyword arguments
 
#mixing keyword and positional arguments
# def name(name,age=20):
#     print("my name is" , name ,"my age is", age)
# name("ayesha")       #20 is the default argument, if i pass argummnet the default parameter will be overwritten

# def display(*args, **kwargs):
#     print(args, kwargs)
# display(23, 56, 23, age = 20, name = "ayesha")
#output is in the form of tupple of; the positional and keyword argument

# def display(*args, **kwargs):
#     print(args, kwargs)
# display(23, 56, 23, age = 20, name = "ayesha", 23)
#error bcz the positional argumnet can't be placed after keyword argument


# def display(*args, **kwargs):
#     print(args, kwargs)
# display(23, 56, 23, age = 20, name = "ayesha")
# val1 = [23, 454]
# val2 = {"name" : "ayesha", "age" : 20}
# display(val1, val2)       #the both arguments are considered as positional arguments

# def display(*args, **kwargs):
#     print(args, kwargs)
# display(23, 56, 23, age = 20, name = "ayesha")
# val1 = [23, 454]
# val2 = {"name" : "ayesha", "age" : 20}
# display(*val1, **val2)   #now its working

#default argument always follows non-defalult, otherwise error occurs

#default arguments on mutabe data types lead to bugs
# def bugs(x = "ayesha", age = 20):
#     print(f"my name is {x} and i am {age} years old!")

# bugs()
# print(bugs.__defaults__)
# bugs()
# print(bugs.__defaults__)
# bugs()
# print(bugs.__defaults__)
# bugs()
# print(bugs.__defaults__)
# bugs()
# print(bugs.__defaults__)
# bugs() 

#the default variables initializes with the same value for every function call.
#but this not happens for mutable data types
# def bugs(name, list = []):
#     list.append(name)
#     print(list)

# bugs("ayesha")
# print(bugs.__defaults__)
# bugs("amna")
# print(bugs.__defaults__)
# bugs("fatima")
# print(bugs.__defaults__)
# bugs("tehreem")
# print(bugs.__defaults__)
# bugs("ali")
# print(bugs.__defaults__)
#default variables are not initializing from start, rather previous one
#to avoid this

# def bugs(name, list = None):
#     if list is None:
#         list = []
#     list.append(name)
#     print(list)

# bugs("ayesha")
# print(bugs.__defaults__)
# bugs("amna")
# print(bugs.__defaults__)
# bugs("fatima")
# print(bugs.__defaults__)
# bugs("tehreem")
# print(bugs.__defaults__)
# bugs("ali")
# print(bugs.__defaults__)

def sum(**kwargs):
    sum = ""
    for x in kwargs.keys():
        sum +=x
    return sum
print(sum(coffee = 23, tea = 100, biscuits = 200))
def sum(**kwargs):
    sum = 0
    for x in kwargs.values():
        sum +=x
    return sum
print(sum(coffee = 23, tea = 100, biscuits = 200))