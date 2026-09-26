class calculator :
    def __init__(self, n):
        self.n = n
    def sq(self):
        print(f"the square is {self.n *self.n}")
    def cube(self):
        print(f"the cube is {self.n * self.n * self.n}")
    def root(self):
        print(f"the squareroot is {self.n ** 1/2}")





a = calculator(4)
a.sq()
a.cube()
a.root()