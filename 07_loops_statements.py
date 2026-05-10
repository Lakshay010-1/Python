# Loops Statements
# 1. while loop
# 2. (i).for loop
#   (ii).for else loop
# 3. Comprehensions

# Loop Control Statements
# 1. break
# 2. continue
# 3. pass

# 1. while loop => Condition-Based Loop,Executes as long as a condition is True.
# Syntax
# while condition:
#     body

idx = 0
while idx <= 5:
    print(idx)
    idx += 1

# while loop on list
list1 = ["Luck", "Light", "Near", "Lawlight", "list"]
i = 0
while i < len(list1):
    print(list1[i])
    i += 1


# 2(i). for loop => Used to iterate over any iterable (list, tuple, string, range, dict, etc.).
# Syntax
# for variable in iterable:
#     body

# range function
for i in range(0, 10, 2):  # range values [0,2,4,6,8]
    print(i, end=" ")
    # 'end' controls what gets printed after each print statement finishes


# Enumerate
# Syntax :
# for index, item in enumerate(iterable):
# pass


for idx, item in enumerate(list1):
    print(f"{idx} => {item}")

# 2(ii). for-else loop => The else block executes only if the loop completes normally (no break).
# Syntax
# for variable in iterable:
#     body
# else:
#     body

tuple1 = (1, 2, 5, 3, 7, "ZERO")
for item in tuple1:
    print(item)
else:
    print("done")
    # this is printed when the loop Completely Executed.


# 3. Comprehension
# Syntax
# expression for item in iterable if condition
# Compreshensions:
# List = [expression for item in iterable if condition]
# Dictionary = {key_expr: value_expr for item in iterable}
# Set = {expression for item in iterable}
# Generator Expression = (expression for item in iterable)
# Nested Comprehensions = [num for row in matrix for num in row]            # let matrix be a 2d list

squares = [x * x for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]


# Loop Control Statements
#   1. ‘break’ is used to come out of the loop when specific condition encountered. It instructs the program to exit the loop.
for i in range(15):
    if i == 13:
        break
        # Exit the loop right when 'i' is equal to 13
    print(i)

#   2. ‘continue’ is used to stop the current iteration of the loop and continue to the next one. It instructs the Program to “skip this iteration”.
for i in range(15):
    if i == 13:
        continue
        # Skip this iteration when 'i' is equal to 13
    print(i)

#   3. 'pass' is a null statement. It instructs to “do nothing”.
for i in range(15):
    pass
    # Placeholder (does nothing)
