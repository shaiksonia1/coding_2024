#Inherientance is a way of creating a new class from an exisiting class

class Employee:
    company = "ITC"
    salary = 45000
    name = "Sonia"
    def show(self):
        print(f"the salary is {self.salary}")

class coder:
    language = "Python"
    company = "ITC Kohinoor"
    def printlanguage(self):
        print(f"the language is {self.language} and the company is {self.company}")

class Programmer(Employee,coder): #this is a inherited class and also single Inheritance
    company  = "ITC infotech"
    def show(self):
        print(f"the name is {self.name}")

# class Programmer(Employee,coder): #this is a inherited class and also mutliple Inheritance
#     company  = "ITC infotech"
#     def show(self):
#         print(f"the name is {self.name}")

a = Employee()
b = Programmer()

b.show()
b.printlanguage()
# print(b.company)
# print(b.language)

'''
Types of Inheritance
1.single Inheritance
1.multiple Inheritance
1.multilevel Inheritance
'''

# Multilevel Inheritance

class Animals:
    a =1
class carniovours(Animals):
    b =2
class omniovours(carniovours):
    c =3

o = Animals()
print(o.a) #prints the attribute
# print(o.b) #shows an error as there is no b attribute in class Animals

o = carniovours()
print(o.a,o.b)

o = omniovours()
print(o.a,o.b,o.c)