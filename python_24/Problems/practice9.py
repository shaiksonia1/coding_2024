f = open("python_24/Problems/poems.txt")
data = f.read()

if("twinkle" in data):
    print("the word twinkle is present")
else:
    print("not present in data")

f.close()