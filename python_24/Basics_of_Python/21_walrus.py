from typing import List,Tuple,Dict,Union
#walrus operator
if (n := len([1,2,3,4,5])) >3:
    print(f"List is too long {n} elements, expected <=3")


#types of definitons
n : int = 5

name : str = "sonia"

def sum(a:int, b:int):
    return a+b


print(sum(3,5))