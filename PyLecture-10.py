# List Comprehension

# What is List Comprehension?
# List comprehension is an elegant way to define and create lists based on
# existing lists.


# msg = "Python Programming"
# items = []
# for ch in msg:
#     if ch == "P" or ch == "i":
#         items.append((ch * 3).upper())  # ["PPP", "PPP", "III"]
#     else:
#         items.append(ch.upper())

# new_msg = "".join(items)
# print(new_msg)


# Syntax 01: [expression for var in iterable]

# Example 01:
# msg = "Python Programming"
# items = [(ch * 3).upper() for ch in msg]  # ["PPP", "yyy"]
# new_msg = "".join(items)
# print(new_msg)

# Syntax 02: [expression for var in iterable if condition]

# msg = "Python Programming"
# items = [(ch * 3).upper() for ch in msg if ch == "P" or ch == "i"]

# new_msg = "".join(items)
# print(new_msg)

# Ternary Operator or Conditional Expression
# Syntax: [true expression if condition else false expression]

# Syntax 03: [expression if condition else expression for var in iterable]

# msg = "Python Programming"
# items = [(ch * 3).upper() if ch == "P" or ch == "i" else ch for ch in msg]

# new_msg = "".join(items)
# print(new_msg)


# Nested List Comprehension

# ----------


# What is a Function?
# A function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.

# Parameters
# A parameter is the variable listed inside the parentheses in the function
# definition.

# Arguments
# An argument is the value that is sent to the function when it is called.

# Return Statement
# The return statement is used to exit a function and go back to the place from
# where it was called.

# Scopes
# A scope is a region of the program and broadly speaking there are three
# places, where variables are stored:
# 1. Local Scope
# 3. Global Scope


# ----------

# x = 50  # global variable

# def test_func():
#     y = 30  # local variable
#     print(x)
#     print(y)

# test_func()
# print(x)
# print(y)


# ---

# x = 50  # global variable


# def test_func():
#     # global x
#     # x = 100
#     x = 100
#     print(x)


# test_func()
# print(x)  # 50


# --

# x = 50  # global variable
# print(hex(id(x)))


# def test_func():
#     print(x)
#     global x
#     x = 100
#     print(hex(id(x)))
#     # print(x)


# test_func()

# print(x)  # 100


# -----

# x = 50
# print(hex(id(x)))
# x = 100
# print(hex(id(x)))


# -----

# x = 50
# # print(hex(id(x)))
# x = 100
# print(hex(id(x)))


# ---

# x = 50
# print(hex(id(x)))
# y = 50
# print(hex(id(y)))


# ----

# students = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25},
# ]

# print(len(students))

# print(students[-1]["name"])

# for student in students:
#     print(student["name"])

# ---

# students = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25},
# ]

# sorted_students = sorted(students, key=lambda x: x["age"])
# print(sorted_students)

# sorted_age_students = []
# sorted_age = []
# for student in students:
#     sorted_age.append(student["age"])
# else:
#     pass

# sorted_age_students = []
# sorted_age = []
# for student in students:
#     sorted_age.append(student["age"])
# else:
#     pass


# Type of Arguments
# 1. Positional Args        Required
# 2. Default Args           Optional
# 3. Keyword Args           Optional
# 4. Variable-length Args   Optional   *args, **kwargs

# --------

# User Defined Function (UDF)
# def add_values(x: int = 30, y: int = 0) -> int:
#     return x + y


# result_values: int = add_values(y=20, x=20)  # Function Calling or Function Execution
# print(result_values)


# ........


# *args     tuple


# def add_values(*nums):
#     # print(type(nums))
#     # print(nums)
#     for num in nums:
#         print(num, end=" ")


# add_values()

# print()
# print(3, 6, True, 3.7, "xyz")


# -------

# result_values = add_values(
#     5, 7, 1, 8, "xyz", True
# )  # Function Calling or Function Execution
# print(result_values)


# ---------

# values = [4, 7, 1, 8, 2]

# add_values = 0
# for value in values:
#     add_values += value

# print(add_values)


# def add_values(*values):
#     total = 0
#     for value in values:
#         if type(value) == int:
#             total += value
#     return total


# result = add_values(3, 7, 8, 1, 8, "xyz", True)
# print(result)


# -----------------


# Functional Programming
# lambda
# map
# filter
# reduce

# Parallel Programming
# zip

# Async Programming
# aysnc, await

# Recursive Programming
# recursion

# Moduler Programming
# module, packages,    functions, classes, global varibales

# Object-Oriented Programming


# Python Advanced Concepts
# 1. Decorator
# 2. Iterator
# 3. Generator

# 4. Comprehension
# 5. Generator Expression

# 6. Regex


# ------

# Functional Programming
# lambda
# map
# filter
# reduce

# User Defined Function (UDF)
# def add_values(x: int = 30, y: int = 0) -> int:
#     return x + y


# # Anonymous Function or Lambda Function
# sum_values = lambda a, b: a + b

# print(sum_values(20, 100))


# students = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25},
# ]


# def sort_by_age(student):
#     return student["age"]


# sorted_students = sorted(students, key=sort_by_age)

# print(sorted_students)
# print(students)

# .......


# students = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25},
# ]

# sorted_students = sorted(students, key=lambda student: student["age"])

# print(sorted_students)

# ---

# from operator import itemgetter

# students = [
#     {"name": "Ahmad", "age": 24},
#     {"name": "Bilal", "age": 27},
#     {"name": "Khalil", "age": 25},
# ]

# sorted_students = sorted(students, key=itemgetter("age"))

# print(sorted_students)

# Bubble Sort
students = [
    {"name": "Ahmad", "age": 24},
    {"name": "Bilal", "age": 27},
    {"name": "Khalil", "age": 25},
]

# Solution ?
