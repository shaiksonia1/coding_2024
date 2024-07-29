#quick quiz
a = int(input("enter a number"))

if(a>=18):
    print("yes")
else:
    print("no")



#p1

b1 = int(input("enter the number"))
b2 = int(input("enter the number"))
b3 = int(input("enter the number"))
b4 = int(input("enter the number"))

if(b1>b2 and b1>b3 and b1>b4):
    print("greatest number is: ",b1)
elif(b2>b1 and b2>b3 and b2>b4):
    print("greatest number is: ",b2)
elif(b3>b1 and b3>b2 and b3>b4):
    print("greatest number is: ",b3)
elif(b4>b1 and b4>b2 and b4>b3):
    print("greatest number is: ",b4)
