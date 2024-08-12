import random
n = random.randint(1,100)
a = -1
guess = 0
while(a!=n):
    a = int(input("Guess a number: "))
    if(a >n):
        print("lower number please")
        guess +=1

    elif(a<n):
        print("higher number please")
        guess +=1

print(f"you have guessed the number {n} in the number of attempts {guess}")