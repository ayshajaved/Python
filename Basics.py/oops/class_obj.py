'''
class has attribute --> variables and behaviour --> functions/methods
'''
'''
in python and java, we can create the object either inside or outside the class but it depends rather the method in python is class or static bcz the static method belongs to the class not to any particular instance/object
'''
# class A():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(self.name, self.age)
#     @staticmethod
#     def inside_class_obj():
#         obj = A("ayesha", 20)
#         obj.show()
# A.inside_class_obj()     #calling the method that makes the object of the class

# class Employee:
#     salary = 500000       #are class attribute
#     language = "python"

# ayesha = Employee()
# ayesha.name = "ayesha"   #instant attribute/object attribute
# ayesha.language= "java"  #instant attribute takes prefernec over the class attribute
# print(ayesha.name, ayesha.salary, ayesha.language)

#making self

# class abc:
#     colour = "orange"
#     area = "34m2"
#     temp = "high"

#     def print():
#         print(f"the colour is {colour} and area is {area} and temp is {temp}")

# ayesha = abc()
# ayesha.print()           #generating an error

# class abc:
#     colour = "orange"
#     area = "34m2"
#     temp = "high"

#     def print(self):
#         print(f"the colour is {self.colour} and area is {self.area} and temp is {self.temp}")
#     @staticmethod 
#     def greet():
#         print("welcome") #this is static method, belongs to the class, and can't access the class varibles bcz it belongs to the class itself
#         #also self is not here so how could we access the variables
# ayesha = abc()
# ayesha.print()          
# ayesha.greet()
# abc.greet()       #class name can be used to call the method that is static

#there is one way to access the variable if in above line the obj is passed, and upper greet method we call ayesha.colour


# class abc:
#     colour = "orange"
#     area = "34m2"
#     temp = "high"

#     def print(self):
#         print(f"the name is {self.name}the colour is {self.colour} and area is {self.area} and temp is {self.temp}")
#     @staticmethod 
#     def greet():
#         print("welcome")

# ayesha = abc()
# ayesha.name="ayesha"
# #the self will print the name
# ayesha.print()          
# ayesha.greet()

# amna = abc()
# amna.print()
# amna.greet()   #but if there are more than one obj it generates error bcz the amna has no attribute name


# class abc:
#     colour = "orange"
#     area = "34m2"
#     temp = "high"

#     def print(self):
#         print(f"the colour is {self.colour} and area is {self.area} and temp is {self.temp}")
#     @staticmethod 
#     def greet():
#         print("welcome")
#     def __init__(self):
#         print("hello")
# #first init is called automatically
# ayesha = abc()
# ayesha.print()          
# ayesha.greet()

# amna=abc()
# amna.print()
# amna.greet()
