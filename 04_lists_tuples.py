# from typing import List, Tuple        #Legacy
from functools import reduce

# 1. List
# 2. Tuple

# List vs Tuple
# Feature	            List (list)	        Tuple (tuple)
# Mutable	            Yes	                No
# Syntax	            [1,2,3]	            (1,2,3)
# Memory usage	        Higher	            Lower
# Speed	                Slightly slower	    Faster
# Methods	            Many	            Few
# Hashable	            No	                Sometimes
# Can be dict key	    No	                Yes (if hashable)
# Dynamic resizing	    Yes	                Fixed size
# Use case	            Changing data	    Fixed/constant data


# 1. Lists
# Lists are containers used to store collections of objects.
# Mutable, Ordered, Indexed, Dynamic array-like data structure
# Data Type = <class 'list'>

# CREATE
empty_list = []
# or empty_list = list()

# typed lists
list2: list[int] = [1, 34, 62, 2, 6, 11]

list1 = ["Apple", "Orange", 5, 345.06, False, "Aakash", "R"]  # heterogeneous data

# READ
first_value = list1[0]
last_value = list1[-1]
sliced_list1 = list[0:2]  # Output: ["Apple", "Orange"]
# list[start:stop:step]

index_of_r = list1.index("R")
# Find position/index of the value


# UPDATE
list1[0] = "Grapes"
# Update value

list1.append("Keyboard")
# Add single value to the list ("Keyboard to the list1")

list1.extend(["Cup", "Earphones"])
# Add multiple values to the list ("Cup","Earphones" to the list1)

list1.insert(3, "RGB")
# Insert at position.
# insert(index,value)


# DELETE
list1.remove("Cup")
# Removes first matching value.

list1.pop()
# Removes by index and returns value.
# Default value -1 (Last value in the list)

del list1[0]
# Remove particular index value

# list1.clear()
# Remove everything


# Sort
list1.sort()
# Doesn't return sorted list
# Default ascending order
# Descending order = sort(reverse = True)
# Custom key = sort(key = len)


list1.sorted()
# Return sorted list
# Same functionality as sort()

# List Comprehension
squared_list = [i * i for i in list2]
# Copying list2 square in new list [squared_list]

# Join
a = ["Rohit", "Ajay", "Lokesh"]
final = "::".join(a)
# output Join list as [Rohit::Ajay::Lokesh]

# Map
square = lambda x: x * x  # lambda function
sqList = map(square, list2)


# Filter
def even(n):
    if n % 2 == 0:
        return True
    return False


onlyEven = filter(even, list2)


# Reduce
def sum(a, b):
    return a + b


mul = lambda x, y: x * y

reduced_sum = reduce(sum, list2)
reduced_multiply = reduce(mul, list2)


# 2. Tuple
# Tuple are containers to store collections of objects.
# Ordered, Fixed(Non-Dynamic), Indexed-based, Im-mutable sequence type
# type : <class 'tuple'>

# CREATE
empty_tuple = ()

# single value tuple
# sin_tuple = (1,)
# valid single value tuple
# The comma defines the tuple.

# sin_tuple = (1)
# invalid single value tuple, this is just int object (1)

data_tuple_1 = (1, 45, 342, 3424, False, False, "Rohan", "Shivam")

data_tuple_2 = 1, 2, 3, 4, 5
# tuple without parentheses
# valid due to : tuple packaging

# Type hints
# Tuple of a string and an integer
# person: Tuple[str, int] = ("Alice", 30)                           #Legacy
person: tuple[str, int] = ("Alice", 30)

# READ

count_frequency_false = data_tuple_1.count(False)
# Count total occurences of the mentioned Element

idx_of_value = data_tuple_1.index(3424)
# Return first occurence index of the mentioned elementvalue_exists_in_tuple_1 = 2 in data_tuple_1

first_data_tuple_1_value = data_tuple_1[0]

last_data_tuple_1_value = data_tuple_1[-1]

data_tuple_1_slice = data_tuple_1[0, 4]


# UPDATE
# data_tuple_1[0] = 100
# Raises: TypeError

# Can update muttable object's value inside tuple
t = ([1, 2], [3, 4])
t[0].append(99)


# DELETE
# No Deletion


# Tuple Packing and Unpacking
# Packing
# Python automatically packs values into tuple.
t = 1, 2, 3

# Unpacking
a, b, c = t
