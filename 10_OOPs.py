# OOPs
# Object-Oriented Programming is a programming paradigm based on objects that encapsulate data (state) and behavior (methods).

# A class defines :
#   - structure,
#   - attributes (data) [Types : Instance Attributes and Class Attributes], and
#   - behavior (Methods - Functions inside classes.) [Types: Static Methods, Class Methods, Magic Methods / Dunder Methods]

# Almost everything in Python is an object (Instance of class).

# Instance is a concrete object created from class
# 'self'    - refers to current object instance
#           - It is automatically passed with a function call from an object.
# 'super'   - Used to access parent implementation

# 4 Pillars
#   1. Encapsulation    : bundling data and methods together.
#   2. Inheritance      : - allows reusing/extending parent class behavior.
#                         - Types : Simple Inheritance, Multilevel Inheritance, Hierarchical Inheritance, and Multiple Inheritance
#                         - Method Resolution Order (MRO) defines the order in which Python searches classes for attributes and methods during inheritance.
#                         - MRO becomes especially important in multiple inheritance, super(), and method overriding.
#                         - Python computes MRO using C3 Linearization Algorithm
#   3. Abstraction      : hide implementation details. (Abstract Base Classes Using 'abc' module)
#   4. Polymorphism     : - different objects to respond to the same interface/method call in different ways.
#                         - Type                      |      Meaning
#                           Method overriding	      |      Child changes parent behavior
#                           Duck typing	              |      Behavior-based polymorphism
#                           Operator overloading	  |      Same operator, different behavior
#                           Function polymorphism	  |      Same function works for many types

# Acess Modifiers
# - Controls how attributes and methods are intended to be accessed
# - Python does not enforce strict private/public.
# - Modifier	|    Syntax	  |   Meaning
#   Public	    |    name	  |   Fully accessible
#   Protected	|    _name	  |   Internal use convention (accessible externally like normal)
#   Private	    |    __name	  |   Name-mangled to reduce accidental access (Internally '__name' becomes '_ClassName__name', externally '_ClassName__name' is accessible like normal)


class Human:

    def walk():
        print("walking")

    def stop():
        print("stopped")

    def work():
        print("working")


# Inheritance
class Employee(Human):
    language = "Python"
    salary = 1200000
    a = 320
    # 'language', 'salary', 'a' are class attribute

    # Constructor (__init__() method / Dunder method)
    def __init__(self, name, salary, language):
        super().__init__()
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an Employee object")

    def getInfo(self):
        print(
            f"Employee's Info:\nName - {self.name}\nlanguage - {self.language}\nsalary - {self.salary}"
        )

    def work(self):
        print("Doing assigned work")

    # static method fn is the function that does not use the self-parameter.
    @staticmethod
    def greet():
        print("Greetings")

    # A class method is a method which is bound to the class and not the object of the class.
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, input_name):
        self.fname = input_name.split(" ")[0]
        self.lname = input_name.split(" ")[1]


# Polymorphism
class Number:
    num = 72

    def __init__(self, n):
        self.n = n

    # Operators Overloading i.e.  a.__add__(b), a.__sub__(b), a.__mul__(b), a.__truediv__(b), a.__floordiv__(b), __len__(), __str__()
    def __add__(self, num):
        return self.n + num.n


# OBJECT

# Empoyee Class Object/Instance
light = Employee("Light Darky", 50000, "Python")

light.emp_id = "95tgy8u9no"
# This is an instance attribute

light.getInfo()
# Same as Employee.getInfo(emp_01)

light.greet()
light.work()


# Number Class Object/Instance
n = Number(99)

print(n.num)
# Prints the class attribute because instance attribute is not present

n.num = 0
# Instance attribute is set

print(n.num)
# Prints the instance attribute because instance attribute is present

print(Number.num)  # Prints the class attribute

a = Number(1)
b = Number(2)

# a + b calls a.__add__(b)
print(a + b)
