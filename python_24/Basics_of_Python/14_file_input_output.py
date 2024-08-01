# f = open("python_24/Basics_of_Python/file.txt")
# data = f.read()
# print(data)
# f.close()


st = "this is the file which will open and write "

f = open("python_24/Basics_of_Python/myfile.txt","w")
data = f.write(st)
print(data)
f.close()