class programmer:
    name = "ayesha"
    @classmethod
    def show(cls):
        print(f"the name of the programmer is {cls.name}")

#object
# a = programmer()
# a.name = "amna"
# print(a.name)
# a.show()
#but if i use the class method then the class atribute will be printed instead of the obj attribute

a = programmer()
a.name = "amna"
a.show() #class method is applied on the method so it prints class attribute
print(a.name)  #important point to know that this prints the obj attribute
