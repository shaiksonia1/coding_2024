#loops
n = int(input("enter a number"))
# using for loop multiplication
for i in range(1,11):
    print(f"{n}x{i} = {n*i}")

# using while loop multiplication
i = 1
while(i<11):
    print(f"{n}x{i} = {n*i}")
    i = i+1

# greet only them whose name starts with "s"
l = ["sonia","raja","shaik","sadia","samreen"]

for i in l:
    if(i.startswith("s")):
        print(f"hi{i}")
    else:
        print("dont greet")


# check if a number is prime number or not
n = int(input("enter a number"))

if(n<=1):
    print("not a prime number")
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime")
        break
    else:
        print("number is prime")

# sum of n natural numbers
n = int(input("enter a number"))
i=1
sum = 0
while(i<=n):
    sum += i
    i +=1
print(sum)

# factorial
n = int(input("enter a number"))
product =1
for i in range(1, n+1):
    product = product * i

print(f"the factorial is {product}")

# start pattern

n = int(input("enter a number"))
for i in range(1, n+1):
    print(" "*(n-i),end="")
    print("*" *(2*i-1), end="")
    print("")

'''
output:
  *
 ***
*****
'''


n = int(input("enter a number"))
for i in range(1, n+1):
    print("*" *(i), end=" ")
    print("")

    '''
    output:
* 
** 
*** 
    
    '''

n = int(input("enter a number"))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*",end="")
        print(" " *(n-2),end ="")
        print("*",end="")

    print(" ")

    '''
    output:
*** 
* * 
*** 
    '''

# multiplication in reverse order
n = int(input("enter a number"))
for i in range(1,11):
    print(f"{n}x{11-i} = {n*(11-i)}")


