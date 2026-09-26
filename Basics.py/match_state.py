'''
alternative to if-else, there are also match statemnets in python, like switch in C
'''
name = "hk"
match name:
    case "ayesha":
        print("true")
    case "amna":
        print("sister")
    case "abdullah":
        print("brother")
    case _:        #default
        print("false")