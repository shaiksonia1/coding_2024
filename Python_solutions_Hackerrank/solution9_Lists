if __name__ == '__main__':  # This ensures the code runs only if the script is executed directly, not when imported
    N = int(input())  # Takes an integer input, representing the number of commands to be executed
    l1 = []  # Initializes an empty list to perform operations on
    
    # Loop through the range of N to execute N commands
    for _ in range(N):
        cmd = map(str, input().split())  # Takes input, splits it into a list of strings, and maps them as strings
        cmd_list = list(cmd)  # Converts the map object into a list for easier access
        
        # Check the first word in the command list to determine the operation
        if cmd_list[0] == 'insert':
            # Inserts the value at the specified position in the list
            l1.insert(int(cmd_list[1]), int(cmd_list[2]))
        elif cmd_list[0] == 'print':
            # Prints the current state of the list
            print(l1)
        elif cmd_list[0] == 'remove':
            # Removes the first occurrence of the specified value from the list
            l1.remove(int(cmd_list[1]))
        elif cmd_list[0] == 'append':
            # Adds the specified value to the end of the list
            l1.append(int(cmd_list[1]))
        elif cmd_list[0] == 'sort':
            # Sorts the list in ascending order
            l1.sort()
        elif cmd_list[0] == 'pop':
            # Removes and returns the last element in the list
            l1.pop()
        elif cmd_list[0] == 'reverse':
            # Reverses the order of elements in the list
            l1.reverse()
