# class company:
#     name = "microsoft"

#     def show(self):
#         print(f"the name is {self.name}")
# class programmer(company):
#     language = "python"

# a = programmer()
# print(a.language, a.name)

#multilevel ineritance (two parents to child)
# class company:
#     name = "microsoft"

#     def show(self):
#         print(f"the name is {self.name}")
# class coder:
#     place = "usa"
# class programmer(company, coder):
#     language = "python"

# a = programmer()
# print(a.language, a.name, a.place)

# parent to child and then to child
# class ayesha:
#     a = 10
# class amna(ayesha):
#     b =23
# class fatima(amna):
#     c =45

# a = fatima
# print(a.c, a.b, a.a)
# b = amna
# print(b.b, b.a)
# c = ayesha
# print(c.a)


class Class:
    def __init__(self):
        print("Welcome!!")
    def show(self, a):
        print(a-10)

demo = Class()
demo.show(34)