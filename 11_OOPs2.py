"""Inheritance-Inheritance is a way of creating a new class from an existing class."""

# Single Level Inheritance- child class inherits only a single parent class.
class Employee:
    company = "ABC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the Company is {self.company}")

class Programmer(Employee):
    company = "ABC_DEF"
    def showLanguage(self):
        print(f"The name is {self.name} and he is expert in {self.language} language")


a = Employee()
b = Programmer()
b.name="Luck"
b.language="Java"
b.show()
b.showLanguage()
print(a.company, b.company)

# Multiple Inheritance-e child class inherits from more than one parent classes.
class Coder():
    language="Rust"

    def __init__(self):
        print("Constructor of Coder")

    def printLanguages(self):
        print(f"Out of all the languages {self.name} excel in : {self.language} language.")

class Discipline():
    level="5"
    
    def __init__(self):
        print("Constructor of Discipline")

    
    def disLevel(self):
        print(f"Level Of discipline is {self.level}")

class Programmer(Discipline, Coder):
    language = "Python"
    
    
    def __init__(self):
        print("Constructor of Programmer")

    
    def showLanguage(self):
        print(f"The name is {self.level} and he is good with {self.language} language")        


pro=Programmer()        
pro.name="Lakshay"
pro.printLanguages()
pro.disLevel()



# Multi-level Inheritance-child class becomes a parent for another child class.
class GrandParents():
    knowledgeLevelGP=10
    
    def __init__(self):
        print("Constructor of GrandParents")

class Parents(GrandParents):
    knowledgeLevelP=7

    def __init__(self):
        super().__init__()
        print("Constructor of Parents")

class child(Parents):
    knowledgeLevelC=5
    
    def __init__(self):
        super().__init__()              #super() method is used to access the methods of a super class in the derived class.
        print("Constructor of Childern")


ch=child()
print(f"Level of Knowledge of \nGrandParents : {ch.knowledgeLevelGP},\nParents : {ch.knowledgeLevelP},\nChildren : {ch.knowledgeLevelC}")