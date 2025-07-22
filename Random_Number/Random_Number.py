import random
num=random.randint(0,9)
guess=int(input("Enter a num in 0-9: "))
while num!=guess:
    if guess<num:
        print("Less num")
        guess=int(input())
    elif guess>num:
        print("Big num")
        guess=int(input())
    else:
        break
print("Bingo")
