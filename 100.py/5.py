'''
1 mile = 0.621 km
1 km = 1000m
i m = 100cm
1 cm = 10 mm
i feet = 12 inches

'''
#leap year
# year = int(input("Enter the year:- "))
# if (year % 400 == 0) and (year %100 == 0):
#     print("leap year!")
# elif(year %4 ==0) and (year %100!=0):
#     print("Leap year!")
# else:
#     print("Not a leap year!")

#map and lambda for squaring
# list1 = []
# for i in range(5):
#     n = int(input("Enter the number in list:-"))
#     list1.append(n)
# result= list(map(lambda n: n**2, list1))
# print(result)

#ord bin hex oct
# decimal = 12
# print(bin(decimal))
# print(oct(decimal))
# print(hex(decimal))

# ch = "a"
# print(ord(ch))

#finding HCF
def hcf(x,y):
    if x >y:
        n = y
    else:
        n = x
    for i in range(1, n+1):
        if (x % i == 0) and (y %i ==0):
            hcfof = i
    return hcfof

        

print(hcf(3,12))