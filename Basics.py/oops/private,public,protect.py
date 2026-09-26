# class room:
#     def __init__(self, mentorname, mentorid, mentorcell):
#         self._mentorname= mentorname  #by _ the mentorname is now protected variable
#         self.__mentorid = mentorid    #by __ the mentorid is private
#         self.mentorcell= mentorcell

#     def show(self):                #mentor name and id is accessible inside class
#         print(f"the mentor name is {self._mentorname}\nthe mentor id is {self.__mentorid}\nthe mentor cell is {self.mentorcell}")
# obj = room("ayesha", "ayeshajaved@", "386427923")
# obj.show()
# print(obj._mentorname)

# #but if i try to access the mentor id individually
# # print(obj.__mentorid()) #it's throwing error. I have to write the class name to access the private variable
# print(obj._room__mentorid)

#if i know the class name, only then i can access the private variables

#encapsulation in oops
'''
it means making the setter and getter. Making one method as setter and one as getter
then calling the setter and setting the variable on run time and then acessing the getter
Getters and setters are methods used to access and modify private attributes of a class.
'''



# class A:
#     def __init__(self):
#         self.__name = None
#     def getting(self):
#         return self.__name
#     def setting(self, name):
#         self.__name = name
# obj = A()
# obj.setting("ayesha")
# print(obj.getting())

#encapsulation
'''
private variables that are not acessible outside the class but inside the class
'''
# class A:
#     def __init__(self):
#         self.__name = "ayesha"

# obj = A()
# print(obj._A__name)
 
#when i tried like below it gives error bcz the show method needs to be called in order to set the self.__name
# class A:
#     def show(self):
#         self.__name = "ayesha"

# obj = A()
# print(obj._A__name)