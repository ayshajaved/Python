'''
Here's a brief overview of these terms in Python:

1. **Iterators**:
   - An iterator is an object that contains a countable number of values and can be iterated upon. It implements the iterator protocol, consisting of the methods `__iter__()` and `__next__()`. The `__next__()` method returns the next value in the sequence, and raises a `StopIteration` exception when there are no more items.

2. **Iterables**:
   - An iterable is an object that can return an iterator. It has an `__iter__()` method that returns an iterator. Examples include lists, tuples, and strings. An iterable can be looped over using a `for` loop or other functions that require iteration.

3. **Generators**:
   - Generators are a special type of iterator created using a function that yields values one at a time. They are defined with a function and the `yield` keyword instead of `return`. Generators produce items only when needed, which makes them memory efficient for large datasets. A generator function returns a generator object that can be iterated over.
'''
#iterator
# list = [1, "ayesha", "javed", 89, 23.4]
# iteration = iter(list)
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# # Using the generator
# gen = my_generator()
# for value in gen:
#     print(value)

# def gen(n):
#     for i in range(n):
#         yield i
# try:
#     generators = gen(4)
#     print(next(generators))
#     print(next(generators))
#     print(next(generators))
#     print(next(generators))
#     print(next(generators))
# except :
#     print("Iteration stops!")

'''
pure and impure/traditional functions
In Python, the concepts of "pure" and "traditional" functions are used to describe different characteristics and behaviors of functions. Let's explore each type:
### Pure Functions
A **pure function** is a function that has the following properties:
1. **Deterministic:** Given the same inputs, a pure function will always produce the same output. This means that the function's output depends solely on its inputs and not on any external state or variables.
2. **No Side Effects:** Pure functions do not cause any side effects. This means they do not modify any external state, such as global variables, files, or data structures that exist outside the function. They only perform computations and return a value.
Because of these properties, pure functions are predictable and easier to test. They are a key concept in functional programming and are often used to create more reliable and maintainable code
def add(a, b):
    return a + b

result = add(3, 4)  # Always returns 7 when called with these inputs
```
In this example, `add` is a pure function because it always returns the same output for the same inputs and does not modify any external state.
### Traditional (Impure) Functions
A **traditional function** (often referred to as an **impure function**) does not adhere strictly to the properties of pure functions. Specifically, traditional functions may have one or both of the following characteristics:
1. **Non-Deterministic:** The output may vary even with the same inputs, usually because the function depends on external state or conditions.
2. **Side Effects:** The function may cause side effects by modifying external variables, performing I/O operations, or interacting with other parts of the program or system.
Traditional functions are common in imperative and object-oriented programming, where functions often need to interact with the program's stae or perform actions beyond returning a value.
#### Example of a Traditional Function
counter = 0
def increment_counter():
    global counter
    counter += 1
    return counter

result1 = increment_counter()  # result1 may vary depending on previous calls
print(result1) #1
result2 = increment_counter()  # result2 may vary depending on previous calls
print(result2) #2
In this example, `increment_counter` is a traditional function because it modifies the external variable `counter`. Its output depends on the external state, making it non-deterministic in the sense that its return value can change even if the function is called with the same inputs (or no inputs, in this case).
- **Pure Functions:** Deterministic, no side effects, and depend only on input parameters.
- **Traditional Functions:** May be non-deterministic and can cause side effects, often interacting with external state or performing I/O.
Understanding the distinction between pure and traditional functions is important for designing predictable, testable, and maintainable code.
'''

'''
comprehensions
4 types in python

'''


'''
print 
help
range
map
filter
sum
sorted
enumerate
zip
open
'''