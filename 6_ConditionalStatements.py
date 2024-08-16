# Conditional Expression
    # if else 
    # if elif else 
    # walrus Operator
    # match statement

# If else statement
age = int(input("Enter your age: "))
if(age>=18):
    print("Adult")
else:
    print("NOT Adult")


# If elif else ladder
if(age>=18):
    print("Adult")
elif(age<=0):
    print("Invalid Age")    
else:
    print("NOT Adult")

# Example
spam1="Click Link".lower()
spam2="Unlimited Money".lower()
spam3="Buy Now".lower()

comment=(input("Comment Here : ")).lower()
if((spam1 in comment) or (spam2 in comment) or (spam3 in comment)):
    print("Spam Comment")
else:
    print("Genuine Comment")

# walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long, contains {n} elements") 

# match Statement
status=int(input("Enter Error Code : "))
match status:  
    case 200: 
         print("OK")
    case 404: 
            print("Not Found")
    case 500: 
            print("Internal Server Error")
    case _: 
            print("Unknown status")


