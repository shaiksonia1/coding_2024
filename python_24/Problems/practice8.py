#p1
def func(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
    else:
        return "none"

    
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))

print(func(a,b,c))

# p2

def func1(f):
    return 5*(f-32)/9

f = int(input("enter the temperature in f : "))
print(f"{func1(f)}degree c")

#p3
n = int(input("enter a number"))
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
print(sum(n))