# Sets are unordered collection of unique elements
#set is a collection of non reptive elements
s = set()
print(type(s))

b = {1,1,1,1,2,34,5,4}
print(type(b))

b.add(566)
b.pop()
print(b)



#union set
s1 = {3,4,5,75,78,865,83}
s2 ={234,64363,3735,45,3}

print(s1.union(s2))

print(s1.intersection(s2))
print(s1.difference(s2))