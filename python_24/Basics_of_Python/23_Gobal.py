# Local variables are those that are defined inside a function.
#  They can only be accessed within that function.


#Global variables are those that are defined outside of any function. 
# They can be accessed and modified by any function in the program

x = 10  # Global variable

def modify_global():
    global x
    x = 20  # Modify global variable

def access_global():
    print(x)  # Access global variable

access_global()  # Output: 10
modify_global()
access_global()  # Output: 20



def local_example():
    y = 5  # Local variable
    print(y)

local_example()  # Output: 5
# print(y)  # Error: y is not defined
