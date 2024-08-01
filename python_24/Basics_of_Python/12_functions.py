#function are basically used to perform a specific task again and again.
#  A programmer can be reused the function by n number of times
# FUNCTIONS

def func():
    print("hello")
func()
func()
func()
func()

def avg():
    a = int(input("enter a number"))
    b = int(input("enter a number"))
    c = int(input("enter a number"))
    average= (a+b+c)/3
    print(average)

avg() #function call
avg()
avg()

def func():

    d=input("enter your name:")

    print(f"{d} Good day!")
func()
func()
func()
func()


# FUNCTION WITH ARGUEMENTS
def func(name,ending):
    print("hi, "+ name )
    print(ending)
func("sonia","thanks")
func("sonia","thanks")
func("sonia","thanks")

#return 
def func(name,ending):
    print("hi, "+ name )
    print(ending)
    return 0
a = func("sonia","thanks")
print(a)

# default value parameter

def func(name,ending = "Thank you"):
    print(f"{name},Good day!")
    print(ending)
func("sonia","thanks")
func("sonia") #this is taking default value which i have assigned in the parameters