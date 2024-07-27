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
num.append(10)
num.pop(1)
num.insert(6,27)
num.insert(5,80)
num.sort()
num.reverse()
num.remove(4)
print(num)
