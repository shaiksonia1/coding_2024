if __name__ == '__main__':
    name_list = []
    score_list = []
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        name_list.append(name)
        score_list.append(score)
    
    # Remove duplicates and sort to find the second-lowest score
    score_list = list(set(score_list))
    score_list.sort()
    
    # Find the second-lowest score
    second_low = score_list[1]
    
    # Extract names of students with the second-lowest score
    num = [i[0] for i in records if i[1] == second_low]
    
    # Sort the names alphabetically
    num.sort()
    
    # Output the names
    for i in num:
        print(i)
