#pq
# dict = {}
# x = int(input("enter phy marks"))
# dict.update({"phy" : x})
# print(dict)

#pq store 9 and 9.0 as seperate values in a set
st = {9,9.0}
print(st)
st = {9,"9.0"}
print(st)
#another way
st= {
    ("int",9),
    ("float",9.0)
}
print(st)