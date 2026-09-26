class Student():
    def __init__(self, name, company, post, lap_name, price):
        self.name = name
        self.company = company
        self.post = post
        self.lap = self.Laptop(lap_name, price) #lap is the obj of the class laptop
    def display(self):
        print(f"Student's name is {self.name} working as {self.post} in the company {self.company}!!")
        self.lap.display()

    class Laptop(): #inner class
        def __init__(self, lap_name, price):
            self.laptopname = lap_name
            self.price = price
        def display(self):
            print("She has laptop {} of price {}".format(self.laptopname, self.price))        

s1 = Student("ayesha","Google" ,"Software engineer", "lenovo", 23000)
s2 = Student("Maheen","Microsoft","Data scientist", "Dell", 34000)
s1.display()
s2.display()