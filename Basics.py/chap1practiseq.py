#taking input from the user and printing their types
age = int(input("enter your age: "))
# name = input("your name: ")
# height = float(input("your height is:"))
# print(type(age))
# print(type(name))
print(type(height))

#q2 taking 2 inputs from the user and printing their sum
# num1 = int(input("enter the first value"))
# num2 = int(input("enter the second value"))
# print("sum is:",num1+num2)
#here the int was necassarily being written as the input returns string so when + was written it just cancatenated not added

#q3 input the int values 
# a = int(input("enter first number : "))
# b = int(input("enter second number : "))
# print(a>=b)

# name = "ayesha"
# age = 20
# height = 5.3
# age , name , height = (20, "ayesha", 5.4)  #another way of declaration
# print(age, name , height)
# print("my name is {name}".format(name = name)) #another way of using te f string
# first = "ayesha"
# last = "javed"
# y = 3
# x = first + last
# print(x)

# z = first +str(y)  #concatenation of a integer by type casting
# print(z)

#in python the memory allocation is of the value not the variable itself like in C
# a = 23
# b = 23
# c = 3
# print(id(a), id(b), id(c))
# #a nd b have same memory

#the division returns the float value but the floor division returns the integer 
# a = 23
# b = 2
# print(a/b)
# print(a//b)

#membership operators in python (in, not in)
# a = "ayesha javed"
# print("s" in a)
# print("s" not in a) 

# #identity operators
# a = 10
# b = 10
# print(a is b, a == b)
# print(a is not b, a != b)

# #bitwise operators
# a = 9
# b = 3
# # #to find there binary values there's a inbuild function
# print(bin(a))
# print(bin(b))
# print(a | b, bin(a | b)) 
# print(a & b, bin(a & b))
# print(a ^ b, bin(a ^ b))

#eval function
# a =int(input('enter the value:')) # if i try to enter the float value it gives the error
# b3 =int(input('enter the value:')) # if i try to enter the float value it gives the error
# a =float(input('enter the value:')) # it can take the int value but it can't take the bnary value
# b =float(input('enter the value:'))
# print(a + b)

# #eval can deal with all types of variables
# a = eval(input("enter:")) # i entered 0b1010 = 10
# b = eval(input("enter:")) # i entered 2

# print(a + b) # returns 12

# a = "i am ayesha javed"
# print(a[:17])          #17 is the length
# print(a[2:10])         
# print(a[:])         
# print(a[-1::-1])         
# print(a[-1:-7:-1])         

a = 3.0
b = 6 
print(a/b)
print(a//b)
print(a*b)

print(2/3)

#understanding __name__
# import _name_main
#output displays the name of this file that is _name_main
# now if i call the function only then it will print the function
# _name_main.display()
# print(__name__)