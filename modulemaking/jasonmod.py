import json
'''
JSON supports mainly 6 data
1.string
2. number
3. boolean
4. null
5. object
6. array

'''
#json is of the string format
#data to json
# dict = {
#     "name" : "ayesha",
#     "age" : 20,
#     "height" : 5.2
# }

# j =json.dumps(dict, indent=10)          #dump is used for files
# print(type(j),j)             


#json to data
# j = '{"name" : "ayesha", "age": 20}'
# n = json.loads(j)
# print(n, type(n))   

# j = '[{"name" : "ayesha", "age": 20}]'
# n = json.loads(j)
# print(n, type(n))   
#the json file may be in list format or dictionary format

#reading from j.json
file = open("D:\PROGRAMMING\python\modulemaking\j.json", "r")
x = file.read()
finaldata= json.loads(x)
print(finaldata)   