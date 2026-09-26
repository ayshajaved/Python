class bike:
    def __init__(self, stock):
        self.stock = stock
        while True:
            in_user = int(input('''
            1)Displaying stock
            2)Rent Bike/s
            3)exit
'''))
            if in_user==1:
                self.display()
            elif in_user==2:
                self.bike_rent()
            else:
                break
    def display(self):
        print(f"The stock available is {self.stock}")
    def bike_rent(self):
        self.n =int(input("Enter the quantity you want:-"))
        if self.n <1:
            print("Plz enter value greater than 1!")
        elif self.n> self.stock:
            print("Sorry! The entered stock is high than availabe!")
        else:
            self.stock -= self.n
            print(f"The amount for your bike number/s {self.n} is {self.n*100}")
            print(f"The stock available is {self.stock}")


obj = bike(100)