# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


s, n = input().split(' ')
n = int(n)  # Convert the string to an integer

# Generate and print combinations for all lengths from 1 to n
for i in range(1, n + 1):
    for combo in combinations(sorted(s), i):
        print(''.join(combo))
