#we will use while loop and for loop
#q print ayesha 5 times
# count = 1
# while count <= 5 :
#     print("hello")
#     count += 1

#q print the numbers 1 to 100
# i = 1
# while i <= 100 :
#     print(i)
#     i+=1

#p print 100 to 1
# i = 100
# while i>= 1:
#     print(i)
#     i-=1

#p print table of n 
# n = int(input("Enter the number to be printed the table: "))
# i = 1
# while i<=10:
#     print(n,"*",i,"=",n * i)
#     i+=1

#p print the elements of the series
#tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# while i<10:
#     print(tup[i])
#     i+=1

# n = int(input("enter num to be matched"))
# i = 0
# while i<10:
#     if(tup[i]==n):
#         print("matched",tup[i])
#         break 
#     else:
#         print("not matched")
#         break 
#     i+=1

#now if there are same two numbers then the above logic won't work bcz of break
# #for the list
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 4, 16, 36)
# n = int(input("enter num to be matched"))
# i = 0
# while i<len(tup):
#     if(tup[i]==n):
#         print("matched",tup[i])
        
#     else:
#         print("not matched")
        
#     i+=1


#p print the series 1 4 9 16 25
# i = 1
# while i <= 10:
#     n = i** 2
#     print(n)
#     tup = (n)
#     i+=1
# # its a tuple so serach a number from the list 
# #num = int(input("enter the number to be searched from the list:"))
# print("tuple is ",tup)

#for loop in tuple
# tup = ("ayesha", "amna", "tehreem", "fatima")
# for values in tup:
#     print(values)

# #in string
# string = "ayesha javed"
# for c in string :
#     print(c)

# #in list
# girls = ["lipstict", "bag", "shoes"]
# for things in girls:
#     print(things)

#for with else
# string = "ayesha javed"
# for c in string :
#     print(c)
# else:
#     print("end")

#but if else is not written that same output happens but it is essential to think whether to use else or not in case of break

string = "ayesha javed"
for c in string :
    print(c)
    # if(c == 'h'):
    #     break
else:
    print("end")

#else part is not executed
#if we erase else then it will be executed

# string = "ayesha javed"
# for c in string :
#     print(c)
#     if(c == 'h'):
#         break

# print("end")

#range()
# s = range(10)
# for i in s:
#     print(i)

for i in range(10):
    print(i)

# for i in range(2, 100, 2):
#     print(i)#printing even values

#printing num from 100 to 1 in range
# for i in range(100, 0, -1):
#     print(i)

# n = int(input("enter n till the sum is to be printed: "))
# i = 1
# sum = 0
# while i<= n:
#     sum = sum +i
#     i+=1
# print(sum)

#q
#factorial of a n
# n = int(input("enter n: "))
# fact = 1
# for i in range(1, n+1, 1):
#     fact = fact * i
# print(fact)
