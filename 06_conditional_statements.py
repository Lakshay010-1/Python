# Comparison Chaining
# Comparison chaining is a feature where multiple comparison operators are combined in a single expression
# and evaluated as a logical chain, not as independent pairwise comparisons.
# Example: (x < y < z) instead of (x < y and y < z)


# Conditional Expression
# if else
# if elif else
# ternary Operator
# walrus Operator
# match statement


# If else statement
spam1 = "Click Link".lower()
spam2 = "Unlimited Money".lower()
spam3 = "Buy Now".lower()
comment = (input("Comment Here : ")).lower()

if comment in [spam1, spam2, spam3]:
    print("Spam Comment")
else:
    print("Genuine Comment")


# If elif else ladder
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
elif age <= 0:
    print("Invalid Age")
else:
    print("NOT Adult")

# Ternary Operator
user_is = "Adult" if (age >= 18) else "Not Adult"

# walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long, contains {n} elements")

# match Statement
status = int(input("Enter Error Code : "))
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status")
