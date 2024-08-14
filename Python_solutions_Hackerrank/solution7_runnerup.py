# Taking input with comma-separated values
user_input = input("Enter elements separated by commas: ")
user_list = user_input.split(',')


print("List with comma-separated values:", user_list)

user_list = list(set(user_list))
user_list.sort()
print(user_list[-2])