import random

def genRand(a, b):
    return random.randint(a, b)

if __name__ == "__main__":
    print("************************************Guess The Number Game************************************")

    a = int(input("Enter the lower limit for the number: "))
    b = int(input("Enter the upper limit for the number: "))
    ran_num = genRand(a,b)

    name1 = input("Player 1 enter your name: ")
    print("Player 1 enter a number: ")

    p1 = int(input())
    at1 = 0

    while p1 != ran_num:
        if p1 < ran_num:
            print("Wrong Answer, please increase the number!")

        else:
            print("Wrong Asnwer, please decrease the number!")

        at1 += 1

        p1 = int(input())

    print(f"Correct answer! You guesses the number in {at1} trials! \n")

    name2 = input("Player 2 enter your name: ")
    print("Player 2 enter a number: ")

    ran_num = genRand(a, b)

    p2 = int(input())
    at2 = 0

    while p2 != ran_num:
        if p2 < ran_num:
            print("Wrong Answer, please increase the number!")

        else:
            print("Wrong Asnwer, please decrease the number!")

        at2 += 1
        p2 = int(input())

    print(f"Correct answer! You guesses the number in {at2} trials!")
    
    if at1 < at2:
        print(f"{name1} won the game! Congratulations {name1}!!")

    elif at1 > at2:
        print(f"{name2} won the game! Congratulations {name2}!!")

    else:
        print("Match Drawn!")