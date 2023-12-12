import random
def number_guesser():
    number = random.randint(0,10)
    response = int(input("enter a number 1-10: "))
    while response != number:
        print("wrong,try again")
        response = int(input("enter a number 1-10: "))
    else:
        print("Correct")

print("######################")

def number_guesser_with_lives():
    lives = 3
    number = random.randint(1,10)
    response = int(input("enter a number 1-10: "))

    if lives == 0:
        print("Game Over")


    while response != number and lives > 0:
        print("Wrong, Try again")
        response = int(input("enter a number 1-10: "))
        lives = lives - 1
        print("you have",lives,"live(s) left")
        if lives < 1:
            print("game over")
        elif lives == 0:
            print("game over")
    else:
            print("Correct")

#print(number_guesser_with_lives())

                   