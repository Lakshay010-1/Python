"""Class"""
#Abstraction, Encapsulation
class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000
    a=320

    def __init__(self, name, salary, language):     # Constructor (__init__() method / Dunder method)
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    #Self Parameter-It is automatically passed with a function call from an object.
    def getInfo(self):
        print(f"The Name is {self.name}.\nThe language is {self.language}.\nThe salary is {self.salary}")

    @staticmethod #static method fn is the function that does not use the self-parameter.
    def greet():
        print("Greetings")

    @classmethod  #A class method is a method which is bound to the class and not the object of the class.
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    
    @property 
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

# Polymorphism
class Number:
    num=72          # This is a class attribute

    def __init__(self, n):
        self.n = n
    # Operators Overloading i.e.  a.__add__(b), a.__sub__(b), a.__mul__(b), a.__truediv__(b), a.__floordiv__(b), __len__(), __str__()
    def __add__(self, num):
        return self.n + num.n

"""Object"""

# lakshay = Employee()
# lakshay.name = "lG Luck" # This is an instance attribute
# lakshay.language="Java"
# print(lakshay.name, lakshay.language, lakshay.salary)
# lakshay.getInfo()     # Same as Employee.getInfo(lakshay)
# lakshay.greet()
# lakshay.show()

# Input Value using Constructor
# dark =Employee("Dark",50000,"Cpp")
# dark.getInfo()
# dark.greet()

n=Number()
print(n.num)            # Prints the class attribute because instance attribute is not present
n.num = 0               # Instance attribute is set
print(n.num)            # Prints the instance attribute because instance attribute is present
print(Number.num)       # Prints the class attribute

a = Number(1)
b = Number(2)

print(a + b)