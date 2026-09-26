'''
variable length arguments
two types:
Variable length positional arguments
variable length kewyword arguments
'''
#variable length positional arguments
# def add(n1, n2):
#     sum = n1+n2
#     return sum
# print(add(23,45))   #but we can pass only two arguments

# def add(*num):
#     print(num) #printing the tuple
#     sum = 0
#     for n in num:
#         sum+=n
#     print(sum)
# add(2,3,3,4)       #we can pass as many as arguments
#actually only one argument is passed in the form of tuple of all the values

#variable length keyword arguments
'''
in this type, the key value pairs are passed(as many as we want) and it is passed as a dictionary
''' 
# def add(**num):
#     print(num)      #returns a dict
#     sums = 0
#     for n in num:
#         sums+=num[n]
#     print(sums) #we have printed the values sum wecan also use the sum function after fetching the values of dict
#     print("*" * 20)
#     print(num.values())
#     return sum(num.values())
    
# print(add(n1= 2, n2= 3, n3= 5))

#we can mix the v.l positionl and keyword arguments
#ordre to use the keywords is:-
'''
positional arguments -> Variable length Positional arguments -> keyword arguments -> variable length keyword argument -> defalut arguments
'''
