import re
#there are two arguments 1)text 2)pattern
# pattern = "is"
# text = '''
# Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, 
# particularly computer systems. It is a field of research in computer science that develops 
# and studies methods and software that enable machines to perceive their environment and use 
# learning and intelligence to take actions that maximize their chances of achieving defined 
# goals.Such machines may be called AIs.
# '''
# result = re.search(pattern, text)
# print(result)

#to find all the occurences of the pattern
# pattern = "is"
# text = '''
# Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, 
# particularly computer systems. It is a field of research in computer science that develops 
# and studies methods and software that enable machines to perceive their environment and use 
# learning and intelligence to take actions that maximize their chances of achieving defined 
# goals.Such machines may be called AIs.
# '''
# result = re.findall(pattern, text) #findall returns the iterator --> list
# print(result, type(result))
# for i in result:
#     print(i)

# iterator 
# pattern = "is"
# text = '''
# Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, 
# particularly computer systems. It is a field of research in computer science that develops 
# and studies methods and software that enable machines to perceive their environment and use 
# learning and intelligence to take actions that maximize their chances of achieving defined 
# goals.Such machines may be called AIs.
# '''
# result = re.finditer(pattern, text) #findall returns the iterator --> list
# print(next(result))
# print(next(result))

# # to find the index also
# pattern = "is"
# text = '''
# Artificial intelligence (AI), in its broadest sense, is intelligence exhibited by machines, 
# particularly computer systems. It is a field of research in computer science that develops 
# and studies methods and software that enable machines to perceive their environment and use 
# learning and intelligence to take actions that maximize their chances of achieving defined 
# goals.Such machines may be called AIs.
# '''
# result = re.finditer(pattern, text) #findall returns the iterator --> list
# for i in result:
#     print(i.group() , i.start(), i.end())  #group() function returns the string matched by the pattern, start gives the starting ndex and end gives the ending index

#matching some difficult pattern
# patern = r"[A-Z]s" #only one ch followed by s, if i write +s, it will find more than one ch
# text = '''
# Artificial intelligence (AI), in its broadest sense, Is intelligence exhibited by machines, particularly computer systems. It Is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.[1] Such machines may be called AIs.
# '''
# match = re.finditer(patern, text)
# print(next(match))
# print(next(match))
# print(next(match))