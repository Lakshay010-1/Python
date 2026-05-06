from functools import reduce

# from typing import List, Tuple #Legacy

# Lists
# Lists are containers to store a set of values of any data type.
# Automatically resizes
# Maintains insertion order
# Data Type = <class 'list'>
# Lists are mutable

list1 = ["Apple", "Orange", 5, 345.06, False, "Aakash", "R"]        # heterogeneous data
list1[0] = "Grapes"
print("List 1 first element : ", list1[0])                          # Access first element
print("List 1 last element : ", list1[-1])                          # Access last element
print("List 1 Slice operation range index 1 to 4 : ", list1[1:4])   # Slice Operation

# typed lists
list2: list[int] = [1, 34, 62, 2, 6, 11]
list2.sort()                                                        # Sort the list in ascending order
list2.reverse()                                                     # Reverse the list
list2.insert(2, 333333)                                             # Insert 333333 at index 2
value = list2.pop(3)                                                # Delete Data at index 3
print("SUM reduce fn -> ", sum(list2))                              # Return sum of the list

# List Comprehension
squaredList = [i * i for i in list2]                                # Copying list2 square in new list [Comprehension]

# Join
a = ["Rohit", "Ajay", "Lokesh"]
final = "::".join(a)                                                # output Join list as [Rohit::Ajay::Lokesh]

# Map
square = lambda x: x * x                                            # lambda function
sqList = map(square, list2)
print("List function of sqList Map : ", list(sqList))


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


# Tuple - Tuple are containers to store a set of values of any data type like lists but unlike lists Tuples are n immutable data type.
emptyTuple = ()
TupleData = (1, 45, 342, 3424, False, False, "Rohan", "Shivam")
print(type(TupleData))                                              # Data Type = <class 'tuple'>

print(TupleData[1])
# TupleData[1]=True                                                 #Tuples are im-mutable

print(TupleData[1:4])

no = TupleData.count(False)                                         # Count total occurences of the mentioned Element
print(no)

i = TupleData.index(3424)                                           # Return first occurence index of the mentioned element
print(i)

print(len(TupleData))                                               # Return length of the tuple

# Type hints
# Tuple of a string and an integer
# person: Tuple[str, int] = ("Alice", 30)                           #Legacy
person: tuple[str, int] = ("Alice", 30)

# Enumerate
enum = [3, 513, 53, 535]
for index, item in enumerate(enum):
    print(f"The item number at index {index} is {item}")
