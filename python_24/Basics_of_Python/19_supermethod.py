class Animals:
    def __init__(self):
        print("constructor of Animals")
    a =1
class carniovours(Animals):
    def __init__(self):
        print("constructor of Carnivouros")
    b =2
class omniovours(carniovours):
    def __init__(self):
        super().__init__()
        print("constructor of omniovours")
    c =3

o = Animals()


o = carniovours()
print(o.a,o.b)

o = omniovours()
print(o.a,o.b,o.c)