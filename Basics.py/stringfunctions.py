# x  = input("enter your name: ")
# print(f"good morning {x}")   #this is the f print function

#string functions
#1 is len
# string = "ayesha"
# print(len(string))
#2 is capitalize
# string = "Ayesha Javed Is a Good Girl"
# print(string.capitalize())
# print(string)   #if we change the original string it would be the same
# print(string.casefold())
#3 replace
# string = "ayesha is a good girl"
# print(string.replace("is","are"))

#4 
# string = "ayesha is a "
# print(string.endswith("ha"))
#5 
# print(string.lower())
# print(string.upper())
#6
# print(string.count("s"))
# print(string.find("are"))
#7
s = "ayesha"
print(s.center(20,"-"))
#8
s = "ayesha\tjaved"
print(s.expandtabs()) 
#9
# s = "ayesha {}"
# print(s.format("javed"))

#10
# s = "ayesha is {n}"
# print(s.format_map({"n":"girl"}))
#11
# s = "ayesha2321"
# print(s.isalnum())
# print(s.isalpha())
# s.is

# a = "ayesha javed"
# print(a.find("z"))     #it will return -1 but the index function returns an erorr if the string is not in parent string

# # print(a.index("z"))
# #we can also pass an argument of where should the checking start
# print(a.index("s", 2))

# #chr() and ord()
# print(chr(68))      #returns the character according to the ascii value

# #reverse is ord
# print(ord("z"))

#format string
print("hello i am {} {}".format("ayesha", "javed"))
print("hello i am {0} {1}".format("ayesha", "javed"))
print("hello i am {1} {0}".format("ayesha", "javed"))
print("hello i am {a} {b}".format(a="ayesha", b = "javed"))
print("hello i am {a:10} and {b}".format(a="ayesha", b = "javed"))
print("hello i am {a:^10} and {b}".format(a="ayesha", b = "javed"))
print("hello i am {a:<10} and {b}".format(a="ayesha", b = "javed"))
print("hello i am {a:>10} and {b}".format(a="ayesha", b = "javed"))
