# variables = container to store a value.
# keywords = reserved words.
# identifiers = class/function/variable name


# Type Annotation
n: int = 5
name: str = "Lakshay"


# type() - type() function is used to find the data type of a given variable
t = type(n)                                                 # <class 'int'>


# Type Casting - convert the Python variable datatype into a certain data type. e.g.-int(), float(), str()
a = str(n)                                                  # <class 'str'>


# Lambda function
square = lambda n: n * n
square_of_5 = square(5)  # Output:25


# Data Types
# (i). Numeric Types
a = 1                                                       # {identifies as <class 'int'>}. # [100_000 is also a valid integer value and interpreted as 100000]
b = 2.98                                                    # {identifies as <class 'float'>}
c = 2 + 7j                                                  # {identifies as <class 'complex'>}

# (ii). Sequence Types
d = "Luck"  # {identifies as <class 'str'>}
e = [1, 2, 3, 4]                                            # {identifies as <class 'list'>}
f = (1, 2, 3, 4)                                            # {identifies as <class 'tuple'>}
g = range(1, 4)                                             # {identifies as <class 'range'>}

# (iii). Mapping Types
h = {"key1": "value1", "key2": "value2"}                    # {identifies as <class 'dict'>}

# (iv). Set Types
i = {1, 2, 3}                                               # {identifies as <class 'set'>}
j = frozenset([1, 2, 3])                                    # {identifies as <class 'frozenset'>}

# (v). Boolean Types
k = True                                                    # {identifies as <class 'bool'>} # [True,False]

# (vi). Binary Types
l = b"hello"                                                # {identifies as <class 'bytes'>}
m = bytearray(5)                                            # {identifies as <class 'bytearray'>}
n = memoryview(b)                                           # {identifies as <class 'memoryview'>}

# (vii). None Types
o = None                                                    # {identifies as <class 'NoneType'>}


# Operators
# (i). Arithmetic operators:
#   Operator	Meaning
#      +	    Addition
#      -	    Subtraction
#      *	    Multiplication
#      /	    Division
#      //	    Floor division
#      %	    Modulus (remainder)
#      **	    Exponentiation	(a^2 is invalid for finding Exponential)
# Example:
n = int(input("Enter Value of n: "))
expo = 3**n                                                 # This computes 3 raised to the power of n
div_float = 3 / 2                                           # Output: 1.5   (float)
div_int = 3 // 2                                            # Output: 1     (int)
round_closest = round(
    div_float
)                                                           # Round the float number to the whole number(increment to the next closest whole number)
round_2_decimal_places = round(
    div_float, 2
)                                                           # Print the float number until n decimal places. e.g. in this case n=2


# (ii). Assignment operators: =, +=, -=, *=, /= etc.
#   Operator	Equivalent
#      =	    	—
#      +=		x = x + 3
#      -=		x = x - 2
#      *=		x = x * 4
#      /=		x = x / 2
#      //=		x = x // 2
#      %=		x = x % 2
#      **=		x = x ** 2
# Example:
n1 = n
n1 += n1
n1 -= 1


# (iii). Comparison operators:
#   Operator	Meaning
#      ==	    Equal to
#      !=	    Not Equal to
#      >	    Greater than
#      <	    Less than
#      >=	    Greater or Equal
#      <=	    Less or Equal
# Example:
equal = 5 == 4
not_equal = 5 != 4
greater = 5 >= 4
smaller = 5 <= 4


# (vi). Logical operators:
#   Operator	Meaning
#      and	    Logical AND
#      or	    Logical OR
#      not	    Logical NOT
# Example:
and_operator = True and False
or_operator = True or False
not_operator = not (and_operator)


# (v). Bitwise operators
#   Operator	Meaning
#      &	    AND
#      |	    OR
#      ^	    XOR
#      ~	    NOT
#      <<	    Left shift
#      >>	    Right shift
# Example:
bit_and = 3 & 5
bit_or = 3 | 5


# (vi). Membership operators
#   Operator	Meaning
#      in	    present in
#      not in	not present in
# Example:
nums = [1, 2, 3]
in_operator = 2 in nums  # True
not_in_operator = 2 not in nums  # True


# (vii). Identity operators
#   Operator	Meaning
#      is	    Check if two variables refer to the same object
#      is not	Check if two variables refer to different objects
# Example:
a = [1, 2]
b = a
print(a is b)  # True


# Operator Precedence and Associativity (In Order of precedence highest to lowest)
#     Operator                                                                                      Associativity
# 1. Parentheses (())                                                                                    -
# 2. Exponentiation (**)                                                                            Right-to-left
# 3. Unary Operators (+x, -x, ~x)                                                                   Right-to-left
# 4. Multiplicative (*, /, //, %)                                                                   Left-to-right
# 5. Additive (+, -)                                                                                Left-to-right
# 6. Bitwise Operators (&, |, ^, <<, >>)                                                            Left-to-right
# 7. Comparison Operators (==, !=, >, <, >=, <=, is, is not, in, not in)                            Chained
# 8. Logical NOt (not)                                                                              Right-to-left
# 8. Logical AND & OR (and, or)                                                                     Left-to-right
# 9. Ternary Operator (value_if_true if condition else value_if_false)                              Right-to-left
# 10. Walrus Operator (:=)                                                                          Right-to-left
# 11. Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=, >>=, <<=)                  Right-to-left
