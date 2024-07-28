#Dictionary is a key value pairs
#we use curly brackets

marks={
    "sonia":34,
     "Ankit":35,
     "Raja":96
}


print(type(marks))

#Dictionary Methods

print(marks.items())
# print(marks.keys())
# print(marks.values())
(marks.update({"sonia" : 89,"ishaq":87}))

# print(marks.get("Ankit2")) #prints 'NONE' bcz the key does not exists in the dictionary``
# print(marks["Ankit2"]) #returns an error
print(marks.popitem()) # removes and returns the last inserted key-value pair as a tuple. If the dictionary is empty, it raises a KeyError
print(marks)