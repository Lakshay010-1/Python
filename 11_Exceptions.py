# Exceptions
# - An exception is an object representing an error or abnormal condition during program execution.
# - Exceptions are objects.
# 'else'    = Runs ONLY if no exception occurs.
# 'finally' = Runs ALWAYS

# Exception Hierarchy
# Most user exceptions inherit from Exception
# All exceptions inherit from: BaseException
# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  ├── GeneratorExit
#  └── Exception
#       ├── ValueError
#       ├── TypeError
#       ├── IndexError
#       ├── KeyError
#       ├── FileNotFoundError
#       ├── ZeroDivisionError
#       └── ...


# try-except + else + finally statement
try:
    a = int(input("Hey, Enter a number: "))
    print(a)
except (ValueError, Exception) as e:
    print(e)
    # e is the exception object.
# except ValueError as v:
#     print(v)
# except Exception as e:
#     print(e)
else:
    print("Success")
finally:
    print("Finished")


# Custom Exception
class InvalidAgeError(Exception):
    print("Age can't be negative")


# Raising Exception
print("Enter numbers to divide")
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))

try:
    if num2 == 0:
        raise ZeroDivisionError(
            "ZeroDivisionError\nInvalid Input\nProgram can't be executed"
        )
    else:
        print(f"Division Result is : {num1/num2}")
except ZeroDivisionError as zde:
    print(f"Error : {zde}")
