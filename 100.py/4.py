#q4 swapping two variables
a = 1
b = 100
temp = a
a = b
b = temp
print(f"a is {a} and b is {b}")

#alternatively simple way
x = 23
y = 45
x, y = y, x          #it is possible in python, but not in C
print(f"x is {x} and y is {y}")

#by function
def swap(a, b):
    a, b = b, a
    return a,b
print(f"a is {swap(33, 89)[0]} and b is {swap(33, 89)[1]}")