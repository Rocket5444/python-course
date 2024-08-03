'''
We all played snake, water gun in our childhood. If you haven't, google the rules of this game and write a 
python program capable of playing this game with me user.
'''
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

computer_choices = list(youDict.values())
computer = random.choice(computer_choices)

youstr = input("Enter your choice: ")
you = youDict.get(youstr)

print(f"You chose {dict[you]}\nComputer chose {reverseDict[computer]}")


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