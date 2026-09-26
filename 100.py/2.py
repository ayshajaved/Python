#Q2 squareroot of a number
#by exponentiation
from typing import Any
a = 256
sq = 256 ** (1/2)
print(f"Sqaure root of {a} is {sq}")

#by user defined variable
x = float(input("Enter the number:-"))
x = x **(1/2)
print("square root is :-", round(x,3))

#by function
def sq(a):
    squareroot= a ** (1/2)
    print(f"Square root of {a} is {squareroot}")
sq(100)

# by oops
class SQ:
    def __init__(self, a):
        self.a = a
    def __call__(self):
        result = self.a ** (1/2)
        print("Sqaure root is", result)

squareroot = SQ(76)
squareroot.__call__()

import math
#by maths library
x = float(input("Enter the number:-"))
print("squareroot is ",math.sqrt(x))