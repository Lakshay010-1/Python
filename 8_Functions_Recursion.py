# Functions-A function is a group of statements performing a specific task.
# Function Definition

def avg():
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    c = int(input("Enter number3: "))    
    average = (a + b + c)/3
    return average

def greet(name="Unknown", ending="Thank You"):
    print(f"Good Day, {name}")
    print(ending)
    return "ok"

def f_to_c(f):
    return 5*(f-32)/9

def removeWord(l, word):
    n = [] 
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

# Function Type Annotation
def  sum(a: int, b: int) -> int:
    return a+b

# Function Call
avg=avg() 
print("Average is ",avg)

msg = greet("Light", "T") 
print(msg)

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")

l = ["Luck","Light", "Near","Lawlight","Dark"]
print(removeWord(l, "an"))

# Recursion
#Recursion Function Definition
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

# Recursion Function Call
num = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(num)}")


