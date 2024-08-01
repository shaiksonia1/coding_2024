#OBJECT ORIENTED PROGRAMMING

#class :Class is a blueprint for creating an object
class Cars:
    model = "BMW" #class Attributes
    color = "White"#class Attributes
    price = 5000000#class Attributes
#self Paramenter:
    def getInfo(self): # Self refers to the instance of the class.It is automatically passed with a function call from an object
        print(f"the color is {self.color}. the price is {self.price}")
        
    # `staticmethod` in Python is a method that belongs to the class rather than an instance and does not access or modify class or instance attributes.
    @staticmethod 
    def head():
        print("hello world")


    #constructor
    def __init__(self,model,color,price):
        self.model = model
        self.color = color
        self.price = price
        print("I am creating an object")
#object: 
 #here BMW and Maruti are the object Instance it has access to the class attributes
BMW = Cars("white","BMW",89000000)
print(BMW.model,BMW.color,BMW.price)

maruti = Cars()
maruti.color = "black" #even though the class attribute is given which is white but the object instance will take preference over class attribute during assignment and reteival 
print(maruti.price,maruti.color)

#self Paramenter
BMW.getInfo()
# maruti.getInfo()

#static method
Cars.head()

#"constructor" Note: You should provide arguments when creating instances unless default values are set in __init__

mercedes = Cars("green","mercedes",600000000)
print(mercedes.model,mercedes.color,mercedes.price)