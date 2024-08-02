class Animals:
    def __init__(self):
        a =1
class carniovours(Animals):
    def __init__(self):
        b =2
class omniovours(carniovours):
    def __init__(self):
        c =1

o = Animals()


o = carniovours()
print(o.a,o.b)

o = omniovours()
print(o.a,o.b,o.c)