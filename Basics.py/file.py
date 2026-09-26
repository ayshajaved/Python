# f = open("ex.txt","r")
# # data = f.read()  #we can pass 5 as a argument to read characters
# # print(data)
# # print(type(data))

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)


# f.close()
#while reading lines there are next line after avery line also there is a important point that when the entire data is read then lines are read it will return empty space bcx the pointer is at end

# f = open("ex1.txt","w")
# f.write("hy! i don't wanna get married so early\nbecause i want to study")
# f.close()

# f = open("ex1.txt","r")
# data = f.read()
# print(data)
# f.close()

#p
# with open("practise.txt","w") as f:
# #     f.write("hey! i love python\ni want to be a python developer\ni love coding\ni love softwares")
# f = open("practise.txt","r")
# data = f.read()
# print(data)
# result = data.replace("python","java")
# print(result)

# f = open("practise.txt","w")
# f.write(result)

# f.close()

# f = open("practise.txt","r")
# data = f.read()
# print(data)

# result = data.find("rrr")
# if(result != -1):
#     print("found")
# else:
#     print("not")
# f.close()

#P WAF to find in which line of the file does the word "learning"occur first.Print -1 if word not found.
# def find():
#     with open("practise.txt","r") as f:
#         data = True
#         word = "java"
#         line =1
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print("word is found")
#                 print(line)
#                 return
#             else:
#                 line+=1
                
                
            
#     return -1

# result = find()
# print(result)

# f = open("practise.txt", "r")
# data = f.read()
# print(data)

# list = data.split(",")
# even = 0
# print(list)
# for values in list:
#     if(int(values)%2==0):
#         even+=1
# print(even)
   
# with open ("practise.txt", "w") as f:
#      f.write('''
# hello i am ayesha
# i am a software engineering student
# i want to become a pro coder!            
#             ''')
    # try:
    #     content = f.read()
    #     for line in content:
    #         print(line) 
    # except:
    #     print("Not readable!")

#error occurs bec when the file is read the pointer is at the last so it is unable too read!
#solution is to use f.seek(0) after reading      
# with open ("practise.txt", "r") as f:  
#     try:
#         content = f.read()
#         print(content)
#         f.seek(0)
#         for line in f:
#             print(line) 
#     except:
#         print("Not readable!")
