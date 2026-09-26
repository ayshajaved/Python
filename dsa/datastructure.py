'''
Data structure is a way to store and organize the data in
effective way to boost operation speeds.
Types of data structures
1. Linear data structures
2. Non - Linear data structures
3. Built-in Data structures
4. user defined data structures
'''
#linera data structures
'''
These data structures stores data elements in
sequential manner. Generally in a contiguous
memory. eg arrays, linked list, stack, queue
linked list as blocks connented, first block us head and last one is null, each bloack contains two boxes first one
is data second one is the memory address of the second block,last block has second box null.
'''

#non linear data structures
'''
No sequential manner.
Data elements are connected with each
other in various ways. eg tree, graph
'''

#builtIn
'''
tuple, dictionary, set, frozenset, list
'''
#user defined
'''
tree, graph, linkedlist and whatever we make by ourselves
'''

#stack data structure
'''
A linear data structure in which elements
are added & deleted only from one end is
called as stack. it follows LIFO principle, last in first out, or first in last out
if we try to push elements in a stack while it is full, then its called stack overflow and underflow if we
try to pop from a empty list
'''

'''
In Python, data structures can be broadly categorized into primitive and non-primitive types based on their complexity and functionality.

### **Primitive Data Structures**

Primitive data structures are the simplest forms of data that are directly supported by the programming language. They represent single values and do not contain other data structures.

1. **Integer (int)**
   - Represents whole numbers, both positive and negative.
   - Example: `10`, `-5`

2. **Float (float)**
   - Represents real numbers and includes decimal points.
   - Example: `3.14`, `-0.001`

3. **Boolean (bool)**
   - Represents two possible values: `True` or `False`.
   - Example: `True`, `False`

4. **String (str)**
   - Represents sequences of characters.
   - Example: `"Hello, World!"`, `'Python'`

### **Non-Primitive (Composite) Data Structures**

Non-primitive data structures are more complex and can store multiple values. They can hold primitive data types or other non-primitive data structures.

1. **List**
   - An ordered, mutable collection of items.
   - Items can be of different data types.
   - Example: `[1, 2, 3, "apple", True]`

2. **Tuple**
   - An ordered, immutable collection of items.
   - Like lists, tuples can contain elements of different data types.
   - Example: `(1, 2, 3, "apple", True)`

3. **Dictionary (dict)**
   - An unordered collection of key-value pairs.
   - Keys are unique, and each key is associated with a value.
   - Example: `{"name": "Alice", "age": 30, "city": "New York"}`

4. **Set**
   - An unordered collection of unique items.
   - Sets are mutable and do not allow duplicate elements.
   - Example: `{1, 2, 3, "apple"}`

5. **Frozenset**
   - An immutable version of a set.
   - Once created, the elements cannot be changed or modified.
   - Example: `frozenset([1, 2, 3, "apple"])`

6. **Complex**
   - Represents complex numbers with a real and an imaginary part.
   - Example: `1 + 2j`, `3 - 4j`
'''
