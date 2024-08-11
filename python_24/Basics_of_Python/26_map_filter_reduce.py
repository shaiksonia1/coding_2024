
from functools import reduce
#map exapmle
#we use map when we want to apply the function to all elements
l = [3,45,56,86,8]

sqaure = lambda x: x*x

sqList = map(sqaure,l)
print(list(sqList))

#filter

def even(n):
    if(n%2==0):
        return True
    return False
onlyeven = filter(even,l)

print(list(onlyeven))

#reduce example

def sum(a,b):
    return a+b
print(reduce(sum,l))