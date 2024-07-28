#  Lists are containers to store set of values of any data type
# Lists are "MUTABLE"
rawdata = ["sonia","ishaq","Insha","raja","Ankit",35.6,32,True]
print(rawdata)

print(rawdata[2])
rawdata[2] ="Shaik"
print(rawdata[2])

# Lists Methods
num = [1,2,3,4,5,6,7,8,9]
print(num)
num.append(10) #will add the element in the end
num.pop(1) # will remove the element
num.insert(6,27) #on the 6th position it will add 27
num.sort() #it will sort in ascending order
num.reverse() #it will reverse the list
num.remove(4)  # it will remove particular element
print(num)
