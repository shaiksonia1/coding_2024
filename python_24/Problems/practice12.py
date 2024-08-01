class Calculator:
    def __init__(self, n ):
        self.n = n
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")
    @staticmethod
    def greet():
        print("hello")

  
a = Calculator(7)
a.square()
a.cube()
a.squareroot()
a.greet()