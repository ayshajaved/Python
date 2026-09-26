'''
there are two conversions in python
implicit:- python does it by itself like int to float
'''
# print(3 == 3.0) #return true, python automatically convert int 3 to float
'''
explicit:- we force python to do
'''
# a = input("enter :-")
# b = input("enter :-")
# print(a + b) #both are string values hence concatenated

# a = input("enter :-")
# b = input("enter :-")
# print(int(a) + int(b)) #both are string values hence concatenated

'''
print() function's arguments
The print() function in Python is used to display output to the console. It can accept several arguments, including:
Objects (positional arguments): The values you want to print. You can pass multiple objects, separated by commas. Each object is converted to a string using str() before being printed.
sep: A string inserted between the objects to be printed. The default value is a single space (' ').
end: A string appended after the last object. The default value is a newline character ('\n'), which moves the cursor to the next line.
file: An object with a write(string) method, like an open file. It defaults to sys.stdout, which means output is printed to the console.
flush: A boolean that specifies whether the output is flushed (True) or buffered (False). The default is False.
print("Hello", "World", sep=", ", end="!", file=sys.stdout, flush=True)
In this example:

"Hello" and "World" are objects to print.
sep=", " specifies that a comma and a space should separate the objects.
end="!" means the output will end with an exclamation mark instead of a newline.
file=sys.stdout directs the output to the console (default behavior).
flush=True forces the output to be flushed immediately.
'''
with open ("hello.txt", "w") as f:
    print("hello ayesha", file = f)

'''
enumerate()
In Python, enumerate() is a built-in function that adds a counter to an iterable and returns it as an 
enumerate object. This enumerate object can then be used in a for loop to retrieve both the index (idx)
and the corresponding item from the iterable.
'''
list1 = ["ayesha", 2, 45.5, "ali"]
for d, i in enumerate(list1):
    print("{0} is index and {1} is member".format(d, i))