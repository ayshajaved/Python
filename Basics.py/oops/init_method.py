# class employee:
#     salary = 20000
#     lang = "java"

#     def __init__(self, name, salary, lang):
#         self.name = name
#         self.salary= salary
#         self.lang=lang
#         print(self.name, self.salary, self.lang)
#     def __init__(self, age):
#         self.age = age
#         print(self.age)
# ayesha = employee("ayesha", 3282742, "python")
# amna = employee(20)
#error bcz in In Java, you can have multiple constructors within a class, each with different parameters (known as constructor overloading). Python, however, does not support multiple constructors in the same way as Java. Instead, Python uses a single __init__ method, which can be designed to handle different initialization scenarios by using default arguments or conditional logic.
#we can handle it by using conditions

class employee:
    salary = 20000
    lang = "java"

    def __init__(self, name, salary, lang, age = None):
        self.name = name
        self.salary= salary
        self.lang=lang
        print(self.name, self.salary, self.lang)
        if age is not None:
            self.age = age
            print(self.age)
ayesha = employee("ayesha", 3282742, "python", 20)
