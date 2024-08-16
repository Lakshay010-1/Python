# variables = container to store a value.
# keywords = reserved words.
# identifiers = class/function/variable name

# Type Annotation
n : int = 5
name: str = "Harry"


# Data Types
a=1         # 'a' is an Integer variable                {identifies 'a' as <class 'int'>}
b=2.98      # 'b' is a Floating Point Number variable   {identifies 'b' as <class 'float'>}
c="Luck"    # 'c' is a String variable                  {identifies 'c' as <class 'str'>}
d=True      # 'd' is a Boolean variable                 {identifies 'd' as <class 'bool'>}
e=None      # 'e' is a None type Variable               {identifies 'e' as <class 'NoneType'>}

# Operators
#(i). Arithmetic operators: +, -, *, /, %, '**'=Exponentiation Operator (a^2 is invalid for finding Exponential) etc.
num=1+2-3*4/5                               #   '*' -> '/' -> '%' -> '+' -> '-'
n=int(input("Enter Value of n: "))
expo=3**n                       # This computes 3 raised to the power of n
print(expo)

#(ii). Assignment operators: =, +=, -=, *=, /= etc.
n1=num
n1+=n1
n1-=1

#(iii). Comparison operators: ==, >, >=, <, != etc.
equalCon = (5==4)
notequalCon = 5!=4
greCon = 5>=4
smlCon = 5<=4

#(vi). Logical operators: and, or, not.
andCon = True and False
orCon =  True or False
notCon1 =  not(andCon)
notCon2 =  not(orCon)

# Type() function and Type Casting

# type() - type() function is used to find the data type of a given variable
t= type(a)      # <class 'int'>

# Type Casting - convert the Python variable datatype into a certain data type. e.g.-int(), float(), str()
a=str(a)        # <class 'str'>

# Taking Input
num1=input("Enter number 1: ")

print("Data type of Number 1 is from ",type(num1))
# "input" take input in string data type

num1=int(num1)                              #Type Casting
num2=int(input("Enter number 2: "))         #Type Casting
sum=num1+num2
print("Sum is : ",sum) 


# Lambda
square=lambda n:n*n
print(square(5))