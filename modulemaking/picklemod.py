import pickle
'''
The pickle module implements a fundamental, but powerful algorithm for serializing and de-
serializing a Python object structure.
You can pickle objects with the following data types:
Booleans,
Integers,
Floats,
Complex numbers,
(normal and Unicode) Strings,
Tuples,
Lists,
Sets, and
Dictionaries.pickle has two main methods. The first one is dump, which dumps an object to a file object and the second
one is load, which loads an object from a file object.
Python pickle functions
dump() — This function is called to serialize an object hierarchy.
load() — This function is called to de-serialize a data stream.

'''
dict = {
    "name" : "ayesha",
    "age"  : 20,
    "degree": "software engineering"    
}

# file = open("p.txt", "wb")
# pickle.dump(dict, file)

file = open("p.txt", "rb")
print(pickle.load(file))

