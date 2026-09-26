class prog:
    a = 2
    def __init__(self):
        print("hello prog")
class coder(prog):
    b=4
    def __init__(self):
        super().__init__()
        print("hello coder")

class company(coder):
    c = 4
    def __init__(self):
        super().__init__()
        print("hello company")

o = company()
print(o.c, o.b, o.a)
