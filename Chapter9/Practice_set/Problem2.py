'''
The game() function in a program lets a user play a game and 
returns the score  as an integer. You need to read a file 'Hi-score.txt' which is either blank or contains the previous 
hi-score.You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
'''

import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("Chapter9/Practice_set/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score: {score}")
    if(score>hiscore or hiscore==""):
        # Write this to the file
        with open("Chapter9/Practice_set/hiscore.txt", "w") as f:
            f.write(str(score))
    return score

game()