#Q3 solving quadratic equation
'''
Quadratic equation is a*x**2 + b*x + c = 0
a,b,c are real numbers and a!=0
'''
from cmath import sqrt
a = float(input("Enter a(a!=0):-"))
b = float(input("Enter b:-"))
c = float(input("Enter c:-"))

#finding discriminat
d = (b**2) - (4*a*c)
root1 = -b - (sqrt(d)/(2*a))
root2 = -b + (sqrt(d)/(2*a))
print("The roots are", root1, "and", root2)

#by function
def quad(a, b, c):
    d = (b**2) - (4*a*c)
    root1 = -b - (sqrt(d)/(2*a))
    root2 = -b + (sqrt(d)/(2*a))
    print("The roots are", root1, "and", root2)

a = float(input("Enter a(a!=0):-"))
b = float(input("Enter b:-"))
c = float(input("Enter c:-"))
quad(a,b,c)