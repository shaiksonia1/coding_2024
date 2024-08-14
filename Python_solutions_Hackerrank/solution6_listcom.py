x = int(input("enter a number"))
y = int(input("enter a number"))
z = int(input("enter a number"))
n = int(input("enter a number"))

num = [[i,j,k]for i in range(0,x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(num)