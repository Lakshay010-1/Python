# Dictionary-Dictionary is a collection of keys-value pairs (unordered, mutable, un-indexed by position,  Cannot contain duplicate keys)
emptyDict = {} 
marks = {
    "Luck": 100,
    "Light": 56,
    "Near": 23,
    0: "Luck",
    "list": [1, 2, 9]

}

# print(marks.keys())
# print(marks.values())
# print(marks.items())
marks.update({"luck": 99, "Dark": 100})
# print(marks.items())


print(marks, type(marks))
# Differnce b/w dict_name.get(Key) and dict_name[key]
# print(marks.get("LawLight")) # Prints None
# print(marks["LawLight"])     # Return Error

#Sets-Set is a collection of non-repetitive elements. (unordered, un-indexed by position, im-mutable, cannot contain duplicate values.)
emptySet = set()
set1= {1, 5, 32, 54,5, 5, 5, "Harry"} 
set1.add(45)
set1.add(45.00)  # 45==45.00 is True as Python considers (45==45.00) as equal in value, even though they are different types.
set1.add(12)
# set1.remove(1)
print(set1)
set1.pop()      # Remove random element from the set.
print(set1,type(set1),"Length of the set1 is : ",len(set1))

s1 = {1, 45, 6, 78}  
s2 = {7, 82, 1, 78}
print(s1.union(s2))
print(s1.intersection(s2))
set1.clear()    # Empties the set.

