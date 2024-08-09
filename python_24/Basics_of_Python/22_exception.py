# The try...except block in Python is used to handle exceptions (errors) 
# that may occur during the execution of a program. This allows the program to continue 
# running even if an error occurs, rather than crashing.
try:
    a = int(input("enter a number : "))
    print(a)
except Exception as e:
    print(e)

print("thank you")

#value error
try:
    a = int(input("enter a number : "))
    print(a)
except ValueError as v:
    print("hey")
    print(v)
except Exception as e:
    print(e)

print("thank you")


#raising exceptions
a = int(input("enter a number1 : "))
b = int(input("enter a number2 : "))

if (b==0):
    raise ZeroDivisionError("hey our program is not meant to divide by zero")
else:
    print(f"the division of a/b is {a/b}")


#try with else

try:
    a = int(input("enter a number : "))
    print(a)

except Exception as e:
    print(e)

else:
    print("i am inside else")


#try with finally

try:
    a = int(input("enter a number : "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("i am inside finally")