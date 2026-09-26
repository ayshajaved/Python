# def add(a, b):
#     return a+b
# print(add(3, 6))
# print(add("ayesha", "javed"))

#function behaves diferently depending upon the arguments or input

#in oops
# class prog:
#     def test(self):
#         print("this is a programming method")

# class coder:
#     def test(self):
#         print("this is the coder method")

# def call(x):
#     x.test()
    
# obj_prog = prog()
# obj_coder= coder()
# call(obj_prog)
# call(obj_coder)

'''
polymorphism means same function name (but different signatures) being uses for
different types.
4 ways to achieve polymorphism
there are two concepts of polymorphism 1) methodoverloading 2)methodoverriding 3)operator overloading 4)ducktyping
overloading is whether we pass the argument or not, the method is same just the functionality differs dependng
•Method overloading is one concept of Polymorphism.
•It comes under the elements of OOPS.
• It is worked in the same method names and different arguments.
•Arguments different will be based on a number of arguments and types of arguments.
'''
# class maths:
#     def area(self, x="", y=""):
#         if x!="" and y!="":
#             print(x*y)
#         elif(x!=""):
#             print(x*x)
#         elif(y!=""):
#             print(y*y)
#         else:
#             print("nothing")

# obj = maths()
# obj.area()
# obj.area(2)
# obj.area(3,4)

# class A:    
#     def __init__(self, name = ""):
#         self.name = name
#         print(self.name)

# obj = A()
# #if i pass the name the name will be printed otherwise empty

# #overriding
'''
•Method Overriding is the method having the same name with the same arguments.
•It is implemented with inheritance also..
•It mostly used for memory reducing processes.
'''
# class A:
#     def display(self):
#         print("class A")
# class B(A):
#     def display(self):
#         super().display()      #without the super, display function of B class only would be printed.
#         print("class B")
# obj = B()
# obj.display()

'''
duck typing
Duck typing is a concept in programming, especially in dynamically typed languages like Python, 
where the type or the class of an object is determined by the methods and properties the object has, 
rather than the object's actual type. The name comes from the phrase "If it looks like a duck, swims 
like a duck, and quacks like a duck, then it probably is a duck." In programming, this means that if 
an object implements the methods and properties expected of a certain type, it can be used as that type.
'''
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_it_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(make_it_speak(dog))  # Output: Woof!
print(make_it_speak(cat))  # Output: Meow!
'''
difference between overriding and ducktyping
### Differences Between Method Overriding and Duck Typing

#### Method Overriding:

1. **Definition:**
   - Method overriding occurs when a subclass provides a specific implementation for a method that is already defined in its superclass.

2. **Inheritance:**
   - Overriding is inherently tied to class inheritance. A method in a subclass overrides a method with the same name in its superclass.

3. **Purpose:**
   - The main purpose of overriding is to provide a specific implementation of a method that is already defined in a parent class, enabling polymorphism.

4. **Static Type Checking:**
   - Overriding methods are known at compile-time in statically typed languages, and at runtime in dynamically typed languages.

5. **Example:**

    ```python
    class Animal:
        def speak(self):
            return "Generic animal sound"

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    animal = Animal()
    dog = Dog()
    cat = Cat()

    print(animal.speak())  # Output: Generic animal sound
    print(dog.speak())     # Output: Woof!
    print(cat.speak())     # Output: Meow!
    ```

    Here, `Dog` and `Cat` override the `speak` method of `Animal`.

#### Duck Typing:

1. **Definition:**
   - Duck typing is a concept where an object's suitability is determined by the presence of certain methods and properties, rather than the object's type itself.

2. **Inheritance:**
   - Duck typing does not require inheritance. Any object that implements the required methods can be used, regardless of its class hierarchy.

3. **Purpose:**
   - The main purpose of duck typing is to allow for more flexible and decoupled code, where objects of different types can be used interchangeably if they implement the same interface.

4. **Dynamic Type Checking:**
   - Duck typing is determined at runtime. The actual type of an object is less important than the methods and properties it implements.

5. **Example:**

    ```python
    class Dog:
        def speak(self):
            return "Woof!"

    class Cat:
        def speak(self):
            return "Meow!"

    def make_it_speak(animal):
        return animal.speak()

    dog = Dog()
    cat = Cat()

    print(make_it_speak(dog))  # Output: Woof!
    print(make_it_speak(cat))  # Output: Meow!
    ```

    Here, `make_it_speak` works with any object that has a `speak` method, demonstrating duck typing.

### Key Differences:

1. **Conceptual Basis:**
   - **Overriding**: Based on inheritance and class hierarchy.
   - **Duck Typing**: Based on the presence of methods and properties regardless of inheritance.

2. **Flexibility:**
   - **Overriding**: Requires a formal relationship between classes (inheritance).
   - **Duck Typing**: Allows for more flexible code, where any object with the required methods can be used.

3. **Implementation:**
   - **Overriding**: Involves subclassing and defining methods with the same signature as in the parent class.
   - **Duck Typing**: Relies on the actual methods present in the objects at runtime.
'''