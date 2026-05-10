# from typing import Dict, Set                                   # Legacy

# 1. Dictionary
# 2. Sets

# 1. Dictionary
# Dictionary is a hash map / associative array implementation that stores data as key → value mappings.
# Insertion Ordered(3.7+), Mutable, Un-indexed by position,  Unique Keys
# type : dict

# CREATE
empty_dictionary = {}
# or empty_dictionary = dict()

# Type hints
# Dictionary with string keys and integer values
scores: dict[str, int] = {"A": 90, "B": 85}

marks = {"Luck": 100, "Light": 56, "Near": 23, "unknown": (1, 2, 9)}
# or marks = dict(Luck= 100, Light= 56, Near= 23, unknown= (1, 2, 9)) -> from key-value pairs
# or marks = dict([("Luck", 100), ("Light", 56), ("Near", 23), ("unknown", (1, 2, 9))])     -> from iterable


# READ
luck_marks = marks["Luck"]
# Raises: KeyError if key missing.

light_marks = marks.get("Light", "DefaultValueHere")
# Safer : returns None or default value, no exception

students = marks.keys()
# Return keys in the dict
# Output: dict_keys(['Luck', 'Light', 'Near', 'unknown'])

students_marks = marks.values()
# Return Values in the dict
# Output: dict_values([100, 56, 23, (1, 2, 9)])

# print(marks.items())


# UPDATE
marks["Lakshay"] = 23
# Add if key doesn't exist, else update

marks.update({"luck": 99, "Dark": 100})
# Multiple Updation


# DELETE
lakshay_marks = marks.pop("Lakshay")
# or del marks["Lakshay"]
# Removes particular key

# marks.clear()
# Removes everything


# Dictionary Comprehension
marks_copy = {
    student_name: student_marks for student_name, student_marks in marks.items()
}

# Dictionary Shallow Copy
marks_shallow_copy = marks.copy()
# or marks_shallow_copy = dict(marks)

# Dictionary Merge
dictionary_one = {"a": 1, "b": 2}
dictionary_two = {"b": 3, "c": 4}
merged_dictionary = dictionary_one | dictionary_two
# or dictionary_one.update(dictionary_two)


# 2. Sets

# (2)(i). Frozen Sets
# - Immutable version of set
# - Cannot: add, remove, update
# - Can be: dictionary keys, set elements
frozen_set_1 = frozenset([1, 2, 3])

# (2)(ii). Sets
# Set is a collection of non-repetitive elements.
# Mutable, un-indexed, unordered collection of unique objects(unique hashable objects implemented using a hash-table-based structure).
# type = <class 'set'>

# CREATE
empty_set = set()
# empty_set = {} creates dictionary, NOT a set

set_1 = {1, 5, 32, 54, 5, 5, 5, "Harry"}
# or set_1 = set([1, 5, 32, 54, 5, 5, 5, "Harry"])

# Set Type hints
s1: set[int] = {1, 45, 6, 78}
s2: set[int] = {7, 82, 1, 78}

# Set Comprehension
s3 = {value for value in set_1}


# READ
# Check Value exists or not
exists = 1 in set_1
# or not_exists = 1 not in set_1

# union
s3_union = s1 | s2
# or s1.union(s2)

# intersection
s3_intersection = s1 & s2
# or s1.intersection(s2)

# difference
s1_s2_difference = s1 - s2
# Elements in first but not second.

# symmertric difference
s1_s2_sym_difference = s1 ^ s2
# Elements in either but not both.

# subset/superset
is_s1_subset_of_s2 = s1.issubset(s2)
# or s1 <= s2

is_s2_superset_of_s1 = s2.issuperset(s1)
# or s2 >= s1

# disjoint sets
# No common elements
is_s1_s2_disjoints = s1.isdisjoint(s2)


# UPDATE
set_1.add(45)
set_1.add(45.00)
# 45==45.00 is True as Python considers (45==45.00) as equal in value, even though they are different types.

set_1.update([4, 5, 6])
# Adds multiple elements.


# DELETE
set_1.remove(1)
# Raises KeyError if value is missing

set_1.discard(1)
# Safer : no error if missing

set_1.pop()
# Remove random element from the set.

# set_1.clear()
# Removes Everything
