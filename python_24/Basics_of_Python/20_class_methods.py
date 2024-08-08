#basically classmethod is used for to access the class attribute when we change the value in object instance
class Employee:
    a =1
    @classmethod
    def show(cls):
        print(f"the value is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45
e.show()

e.name = "sonia shaik"
print(e.fname, e.lname)

