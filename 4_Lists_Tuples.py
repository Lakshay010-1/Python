from functools import reduce
from typing import List, Tuple

# List - Lists are containers to store a set of values of any data type.
emptyList=[]
list1 = ["Apple", "Orange", 5, 345.06, False, "Aakash", "R"]
print(type(list1))              #Data Type = <class 'list'>         

print(list1[0])
list1[0] = "Grapes"             #Lists are mutable
print(list1[0])

print(list1[1:4])

list1.append("Harry")
print(list1)

list2 = [1, 34,62, 2, 6, 11]
list2.sort()                   #Sort the list in ascending order
list2.reverse()                #Reverse the list
list2.insert(2, 333333)        # Insert 333333 at index 2
value = list2.pop(3)           # Delete Data at index 3
print(sum(list2))              # Return sum of the list 
print(value)
print(list2)

# Type hints
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# List Comprehension
myList = [1, 2, 9, 5, 3, 5]
squaredList = [i*i for i in myList]         #Copying myList square in new list [Comprehension]

print(squaredList)

# Join
a = ["Rohit", "Ajay", "Lokesh"]
final = "::".join(a)
print(final)                                # output Join list as [Rohit::Ajay::Lokesh]


# Map 
list3 = [1, 2, 3, 4, 5]

square = lambda x: x*x
sqList = map(square, list3)
print(list(sqList))

# Filter 
def even(n):
    if (n%2 == 0):
        return True 
    return False

onlyEven= filter(even, list3)
print(list(onlyEven))

# Reduce 
def sum(a, b):
    return a + b

mul = lambda x,y:x*y

print("Sum is: ",reduce(sum, list3))
print("Product is: ",reduce(mul, list3))










# Tuple - Tuple are containers to store a set of values of any data type like lists but unlike lists Tuples are n immutable data type.
emptyTuple=()
TupleData = (1,45,342,3424,False,False, "Rohan", "Shivam")
print(type(TupleData))          #Data Type = <class 'tuple'>

print(TupleData[1])               
#TupleData[1]=True              #Tuples are im-mutable    

print(TupleData[1:4])

no = TupleData.count(False)     #Count total occurences of the mentioned Element
print(no)

i = TupleData.index(3424)       #Return first occurence index of the mentioned element
print(i)

print(len(TupleData))           #Return length of the tuple

# Type hints
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)

# Enumerate
enum = [3, 513, 53, 535]
for index, item in enumerate(enum):
    print(f"The item number at index {index} is {item}")