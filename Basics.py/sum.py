class employee:
    company = "microsoft"
    salary = 100000

    def info(self):
        print(f"the company is {self.company}\nthe salary is {self.salary}")
    def __init__(self, name, salary, comany):
        self.name = name
        self.salary= salary
        self.company=comany 
        print(self.name, self.salary, self.company)
    @staticmethod
    def hello():
        print("hello!")
        


o1 = employee("amna", 100000, "microsoft")
o1.hello()
o2 = employee("fatima",12983, "google")
o2.hello()
# o1.info()

# o2 = employee()
# o2.name = "ayesha"
# print(o2.name)
# o2.info()   
