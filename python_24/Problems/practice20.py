#User will input (3ages).Find the oldest one

num1 = int(input("enter a age"))
num2 = int(input("enter a age"))
num3 = int(input("enter a age"))

if num1 > num2 and num1 >num3:
    print(num1)
elif num2>num3 and num2 > num3:
    print(num2)
elif num3>num1 and num3> num2:
    print(num3)
elif num1 == num2 == num3:
    print("same age")
else:
    print("There is a tie between some ages.")