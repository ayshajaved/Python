#there are two types of errors
'''
logical errors and syntax errors; we can handle the logical error but we can't handle syntax error, except to correct it
'''
# n = int(input("Enter n:- "))            #if i enter ajdsfhks in the input it gives value error
# for i in range(1, 11):
#     print(f"{n} * {i} = {n*i}")
# try:
#     n = int(input("Enter n:- "))            
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n*i}")
# except ValueError:
#     print("there is a value error")
# except IndexError:
#     print("There is a index error")
'''
zerodivisionerror
numdivision
typeerror
keyerror
modulenotfinderror
importerror
In Python, except Exception as obj: is used in a try-except block to catch exceptions and handle errors gracefully. Here's a breakdown of how it works:
Exception: This is the base class for all built-in exceptions in Python. When you catch Exception, you are catching all exceptions that are subclasses of Exception, which includes most of the standard exceptions, like ValueError, TypeError, IOError, etc.
as obj:: This part assigns the caught exception to the variable obj. This allows you to access information about the exception, such as the error message, traceback, or any other attributes specific to that exception.
'''
try:
    n = input("enter numer to be the denometor, the numerator is 10:")
    result = 10/n
    print(result)
except Exception as obj:
    print(f"the error is {obj}")


