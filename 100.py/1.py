#Q1 sum of two numbers
#by pre-defined variables
a = 23
b = 21
print("sum of a and b is:-",a+b)

#by user defined variables
x = float(input("Enter first number:-"))
y = float(input("Enter second number:-"))
print("Sum of numbers is:-", x+y)

#by function
def add(a,b):
    return a+b
print("Sum is :- ",add(4,6))

# by oops

class add:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def adding_num(self):
        print("Sum is:-", self.a + self.b)
add_object = add(4,6)
add_object.adding_num()

#by __call__() method
class add:
    def __call__(self, *args):
        return sum(args)
adding = add()
print(adding.__call__(3,5))