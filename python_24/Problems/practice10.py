import random

def game():
    print("you are playing this game")
    score = random.randint(1,100)

    #fetch the highscore
    with open("python_24/Problems/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"your score : {score}")
    if(score>hiscore):
        with open("python_24/Problems/hiscore.txt","w") as f:
            f.write(str(score))

    return score

game()