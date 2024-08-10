l =[2,5456,7,8,87,36,]

# index =0 
# for item in l:
#     print(f"the item number at index {index}is {item}")
#     index +=1

# but we can do this by enumerate 
for index, item in enumerate(l):
    print(f"the item number at index {index}is {item}")


#list Comphrensions
mylist = [3,345,8,9876543,5678]

# squaredlist = []
# for item in mylist:
#     squaredlist.append(item*item)

squaredlist = [i*i for i in mylist]

print(squaredlist)