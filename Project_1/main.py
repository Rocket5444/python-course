'''
1 for snake
-1 for water
0 for gun
'''
import random

def play_game():

    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "snake", -1: "water", 0: "gun"}

    computer_choices = list(youDict.values())
    computer = random.choice(computer_choices)

    youstr = input("Enter your choice: ")
    you = youDict.get(youstr)

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


    if(computer == you):
        print("It's a draw")

    else:
        if(computer ==-1 and you ==1):
            print( "You win!")

        elif(computer ==-1 and you ==0):
            print("You lose!")

        elif(computer ==1 and you ==-1):
            print("You lose!")

        elif(computer ==1 and you ==0):
            print("You win!")

        elif(computer ==0 and you ==-1):
            print("You win!")

        elif(computer ==0 and you ==1):
            print("You lose!")

        else:
            print("Something went wrong!")

while True:
     play_game()
     play_again = input("Do you want to play again?(y/n): ").lower()

     if(play_again != "yes"):
         print( "Thanks for playing!")

         break


