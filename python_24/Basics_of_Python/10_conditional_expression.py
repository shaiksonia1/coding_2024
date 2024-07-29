#if else elif ladder

a = int(input("enter youe age : "))

if(a>=18):
    print("you are eligible to vote. ")
elif(a==0):
    print("you are entering 0 which is invalid age. ")
elif(a<0):
    print("enter the valid age it is in negavtive which you have entered.")
else:
    print("you are not eligible to vote")

print("ended")


# if-else conditional
b = int(input("enter your salary : "))

if(b>=25000):
    print("you can go out side and enjoy")
else:
    print("you are low with your salary")