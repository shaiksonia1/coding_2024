# # #WAP to store seven fruits in a list entered byt he user.
# # #p

fruits = []
f1 = input("enter fruit name")
fruits.append(f1)
f2 = input("enter fruit name")
fruits.append(f2)
f3 = input("enter fruit name")
fruits.append(f3)
f4 = input("enter fruit name")
fruits.append(f4)
f5 = input("enter fruit name")
fruits.append(f5)
f6= input("enter fruit name")
fruits.append(f6)
f1 = input("enter fruit name")
fruits.append(7)
print(fruits)


# # #p2
# # # WAP to accept marks of 6 students and display them in a sorted manner

marks =[]
m1 = int(input("enter marks"))
marks.append(m1)

m2 = int(input("enter marks"))
marks.append(m2)

m3 = int(input("enter marks"))
marks.append(m3)

m4 = int(input("enter marks"))
marks.append(m4)

m5 = int(input("enter marks"))
marks.append(m5)

m6 = int(input("enter marks"))
marks.append(m6)

marks.sort()
print(marks)

# #p3

# # check that tuple can not be changed

a = (34,"sonia",35)
a[2]="shaik"
print(a) #output :'tuple' object does not support item assignment

#p4
#wap to sum a list with 4numbers

num1 =[1,2,3,4]
print(sum(num1))

#p5

a = (7,0,8,0,0,9)
print(a.count(0))