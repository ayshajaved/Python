class a :
    def show(self):
        print("class a")

class b:
    
    def show(self):
        print("class b")

class c(b,a): # if i write "a" the "b" the class a would be printed
    pass

object = c()
object.show()