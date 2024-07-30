#for loop
for i in range(1,6):
    print(i)

#while loop

i = 1
while(i<51):
    print(i)
    i +=1


#while loop example
# ex:1
l = ["sonia",12,4,3,"shaik"]
i=0
while(i<len(l)):
    print(l[i])
    i = i+1

# ex:2
for i in range(1,20,5):
    print(i)

#for loop with list
l =[1,23,24,46,467,85,3,35,765] 
for i in l:
    print(i)

#for loop with tuple
t = (342,525,346,63,56,23) 
for i in t:
    print(i)

#for loop with string 
s = "sonia" 
for i in s:
    print(i)

#for loop with else
li = [2,3,45,4]

for i in li:
    print(i)
else:
    print("done")

#the break statement

for i in range(1,100):
    if(i == 55):
        break #exit the loop right now
    print(i)

for i in range(1,100):
    if(i == 55):
        continue # skip the iteration and continue with the loop
    print(i)


for i in range(23,242):
    pass