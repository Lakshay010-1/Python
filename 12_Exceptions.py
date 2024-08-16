# Exceptions


# try-except statement
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Error Found")
    print(v)
    
except Exception as e:
    print(e) 

print("Success")


# Raising Exception
num1=int(input("Enter Number 1 : "))
num2=int(input("Enter Number 2 : "))

if(num2==0):
    raise ZeroDivisionError("Program can't be executed.")
else:
    print(f"Division Result is {num1/num2}")


# Try else statement
try:
    a = int(input("Enter a number: "))
    print(a)    
except Exception as e:
    print(e) 
else:                                   #else block is executed after successfully executing try block
    print("Try block successfully Executed")


# Finally
def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
        
    except Exception as e:
        print(e) 
        return
    finally:
        print("Finally Block")


main()                                      #Main Function Call


# Global
number=23

def fun():
    # global number
    number=3
    print(number)

fun()
print(number)    