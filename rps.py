import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    player_choice = input("\nEnter ... \n1. for Rock\n2. for Paper\n3. for Scissors:\n\n")

    player = int(player_choice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3.")

    computer_choice = random.choice("123")

    computer = int(computer_choice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.","").title() + ".")
    print("Computer chose " + str(RPS(computer)).replace("RPS.","").title() + ".\n")

    if player == 1 and computer == 3:
        print("🎉You win!🎉")
    elif player == 2 and computer == 1:
        print("🎉You win!🎉")
    elif player == 3 and computer == 2:
        print("🎉You win!🎉")
    elif player == computer:
        print("👌Draw!👌")
    else:
        print("👀Computer wins!👀")
    
    playagain = input("\nPlay again?\nY for Yes\nQ to Quit \n\n")
    if playagain.lower()=="y":
        continue
    else:
        print("\n🎉\n")
        print("Thank u for playing")
        playagain = False

sys.exit("Bye! 👏")