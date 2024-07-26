#  string is a data type in python

# string is a sequence of characters enclosed in quotes

a = 'Shaik'

b = "Sonia"

c = '''Ali'''

print(a,b,c)

# string is immutable means we cannot change the existing string 
# for example in sonia we cannot chane a particular letter n as p

# In string the index starts from 0 and length from 1
# in reverse it will be -1,-2.... index

Name = "shaik"

shortname = Name[0:4] #starts from the 0 index all the way to 4 (excluding 4) means output will be :shai
print(shortname)

# Negative indices

name1 = "shaikshafi"

shortname1 = name1[-10:-2]
print(shortname1)

print(Name[:4])
print(Name[1:])

# slicing with skip value

skip = "abcdefghijklmnopqrstuvwxyz"

skip1 = skip[1:11:1]
print(skip1)