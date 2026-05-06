# Functions:
#   Functions are first-class objects used to encapsulate reusable logic.
#   Group of statements performing a specific task.
#   They support flexible parameter passing, multiple return styles, closures, decorators, and more.
#   Can return multiple values (tuple packing).

# Functions & Methods
#   Functions → standalone
#   Methods → belongs to a class

# First Class Functions
#   Assigned to variables
#   Passed as arguments
#   Returned from other functions

# Higher Order Functions
#   Functions that take/return functions

# Function Definition
# Syntax:
# def function_name(parameters):
#     """optional docstring"""                                          # Explains the purpose of the function, accessed using function_name.__doc__
#     # body
#     return value

# Function Call
# function_name(name)

# Type of Functions
# 1. Built-in
name_length = len("name")


# 2. User-Defined
def avg():
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    c = int(input("Enter number3: "))
    average = (a + b + c) / 3
    return average


# 3. Lambda Function
square = lambda x: x * x


# Parameters and Arguments
# (Python requires this order rule :-  Positional arguments must come before keyword arguments)
# fn(a,b): pass


# 1. Default Parameters
def greet(name="Unknown", ending="Thank You"):
    print(f"Good Day, {name}")
    print(ending, end="\n\n")
    return "ok"


greet()

# 2. Positional arguments
# - Arguments that are assigned to parameters based on their position (order).
# - Example : fn(1,2)
# In this fn call a is equal to 1 and b equals to 2.
greet("Light", "Bye World!")

# 3. Keyword arguments
# - arguments where you explicitly specify the parameter name (order doesn't matter).
# - Example : fn(b=1,a=2)
# In this a equals to 2 and b is equals to 1.
greet(ending="Hello World!", name="L")


# Function Type Annotation
def sum(a: int, b: int) -> int:
    return a + b


a = int(input("Enter 'a' number  : "))
b = int(input("Enter 'b' number  : "))
print(f"Sum of a and b is {sum(a,b)}", end="\n\n")


# Recursion
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


num = int(input("Enter a number to calculate its factorial : "))
print(f"The factorial of this number is: {factorial(num)}\n")
