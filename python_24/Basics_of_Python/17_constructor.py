#constructors
# In Python, a constructor is a special method `__init__` used to initialize a newly created object.
class Dogs:
    Breed = "Shihtzu" #it is a class attribute
    weight = "7kg"
    color = "black"
   
    def __init__(self,Breed,weight,color): #we have created a constructor with init method
        self.Breed = Breed #we have created instance attributes
        self.color = color #we have created instance attributes
        self.weight = weight #we have created instance attributes
        print("i am creating an object")

shihtzu = Dogs("labrador","25kg","gold") #creating instance
print(shihtzu.Breed,shihtzu.color,shihtzu.weight)

labs = Dogs("labrador","30kg","white") #creating new instances
print(labs.Breed,labs.color,labs.weight)

beagle = Dogs("Beagle", "10kg", "brown")
print(beagle.Breed, beagle.color, beagle.weight)