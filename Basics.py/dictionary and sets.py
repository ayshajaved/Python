dict = {
"name" : "ayesha" ,
"age"  :  20,
"height": 5.4,
"subj" : ["chem","phy","bio"]# we can't take list or dictionary as key bcz they are mutatble
}

# print(dict)

# print(dict["name"])
# print(dict["subj"])
# dict["surname"] = "aj"
# print(dict)

# #nested dictionary
# dict = {
# "name" : "ayesha",
# "age"  : 20,
# "sub"  : {
#     "phy" : 23,
#     "chem": 45,
#     }          #i want to store the respective marks in the subjects
#  }

# print(type(dict))
# print(len(dict))
# print(dict["sub"]["chem"])

# print(list(dict.keys()))
# result= dict.values()         #result is in the form ofa list, and on list we can apply the sum function
# print(result, type(result))
# print(dict.items())
# print(dict.get("name"))
# #print(dict["name2"])      #error
# print(dict.get("name2"))

# dict.update({"name" : "ajj"})
# print(dict)
# dict.update({"city" : "jhang"})
# print(dict)


#creating null dictionary
#dict = {}

# d = {
#     "name" :"ayesha",
#     "age"  : 20
#     }
# # a= d["age"]
# print(a)

# del d["age"]
# print(d)

# delete = d.pop("name")   #it also returns the value
# print(delete)
# print(d)

#dict()
#we can also make the dictionary using dict() function

# d = dict(name = "ayesha", age = 20, inst= "cui")
# print(d)



#sets
# set = {1,2,3,4,2}
# print(set)
# print(type(set))
#empty set
# sets = set()
# print(type(sets))
# sets.add(1)
# sets.add(2)
# sets.add(2)
# print(sets)
# set1 = {1,2,3}
# sets.union(set1)


# set1 = {1,2,3,4,5,3,3,2}
# set2 = {2,3,23,4,5,6}
# print(set1.union(set2))
# #or 
# print(set1 | set2)
# print(set1.intersection(set2))
# #also by and &
# print(set1 & set2)
# print(set1.symmetric_difference(set2))      #elements that are in set1 or set 2 but not in both
# #list or tuple to a set
# list = [23, 45, 23, 89]
# tup= (23, 45 , 23, 98)
# a = set(list)
# b = set(tup)
# print(a, b)

# #pq1
# dict = {
# "table" : ["a piece of table" , "a fact"],
# "chair" : "black",

# }

# print(dict["table"])

# #pq2
# #suppose their are different languages and one class room can be used for one language so tell how many classes will be consumed
# set = {"python", "c" , "c++", "c","python", "java", "javascript","c"}
# print("the no of classes are =", len(set))

#p3
# set = {1, 1.0, "1"}
# print(set)
# print(type(set))
# print(len(set))
#we can print the set index
# set1 = {23, 45, 56.6, "ayesha"}
# print(set1[2])
# throws an error because set is unorderd

set1 = { 11,"water", -1 }

set1.add(25)

print(set1)#




#list of dictionaries

# people = [
#     {"name" : "ayesha", 
#      "age"  : 20},
#     {"name" : "amna",
#      "age"  : 17
#     } 
# ]

# print(people)
# print(people[0]["age"])

d = {}
d.update({"id" : 12, "name" : "ayesha"})
for i in d:
    print(i, d[i])