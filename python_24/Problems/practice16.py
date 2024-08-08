class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"the vector is {self.i} + {self.j} ")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"the vector is {self.i} + {self.j} + {self.k}")

a = TwoDvector(1,2)
a.show()
b = ThreeDvector(1,2,3)
b.show()


#p2
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow")
d = Dog()
d.bark()

#p3

class Employee:
    pass
e = Employee()
e.salary = 345
e.incremwnt =20