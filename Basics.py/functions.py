# #function definition for sum
# def sum(a,b):
#     sum = a+b
#     return sum

# #function call
# result=sum(3,5)
# print(result)

# def average(a,b,c):
#     sum = a+b+c
#     av = sum/3
#     return av

# result = average(2,3,4)
# print(result)

#print function
# print("ayesha","javed")#even though i don't give the space between ayesha and javed it executed a space so this is sep parameter working
# print("ayesha")#end is defined as the next line but we can change the end value
# print("javed")

# print("ayesha",end="&")
# print("javed")#interesting

#default parameters
# def calsum(a=1,b=1):
#     sum = a+b
#     return sum
# result =calsum()
# print(result)

# def calsum(a,b=1):
#     sum = a+b
#     return sum
# result =calsum(3)
# print(result)

#p write a program a print the length of a list and list is a parameter
# def leng(list):
#     i = 0
#     while i<len(list):
#         print(list[i],end=" ")
#         i+=1
# list = ["ayesha", "javed", "is", "here"]
# leng(list)

#by for loop
def ele(list):
    for el in list:
        print(list,end=" ")

names = ["a","b","c","d","e"]
ele(names)