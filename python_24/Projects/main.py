'''
#snake water gun game

1 for snake
-1 for water
0 gun


This code implements a simple game where the user and the computer choose between "snake" (`1`), 
"water" (`-1`), and "gun" (`0`). The computer's choice is randomly selected using `random.choice([-1, 0, 1])`,
and the user inputs their choice as a character (`'s'`, `'w'`, or `'g'`). These choices are mapped to their
corresponding integers using dictionaries. The program then prints both choices and determines the outcome based on predefined rules:
if the choices are the same, it's a draw; otherwise, it checks specific conditions to declare if the user wins or loses.
'''

import random 

computer = random.choice([-1,0,1])
yourstr = input("enter your choice")
your_dict = {"s":1, "w":-1 , "g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}

you = your_dict[yourstr]
print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("its a draw")
else:
    if(computer == -1 and you == 1):
        print("you win!")

    elif(computer == -1 and you ==0):
        print("you lose")

    elif(computer == 1 and you ==-1):
        print("you lose")

    elif(computer == 1 and you == 0 ):
        print("you win")

    elif(computer == 0 and you == -1 ):
        print("you win")

    elif(computer == 0 and you == 1 ):
        print("you lose")

    else:
        print("something went wrong")