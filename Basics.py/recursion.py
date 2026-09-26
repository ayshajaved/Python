# def show(n):
#     print(n)
    
# show(10)
#converting into a recursive function
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("end")

# show(5)

#recursive function to print sum of n natural num
# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1) + n
# print(sum(3))

#print the fact
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return fact(n-1) * n 

# print(fact(3))

#print the elements of a list
# def print_list(list, index):
#     if(index == len(list)):
#         return
#     print(list[index])
#     print_list(list , index+1)

# fruits = ["apple","banana","mango","appricot"]
# print_list(fruits,0)

#reverse
# def reversal(str):
#     if len(str)==1:
#         return str
#     else:
#         return reversal(str[1:]) + str[0]
# print(reversal("hello"))

counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

result1 = increment_counter()  # result1 may vary depending on previous calls
print(result1)
result2 = increment_counter()  # result2 may vary depending on previous calls
print(result2)

