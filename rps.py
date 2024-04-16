import sys
import random
from enum import Enum

def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3


    player_choice = input("\nEnter ... \n1. for Rock\n2. for Paper\n3. for Scissors:\n\n")

    if player_choice not in ["1", "2", "3"]:
        print("You must enter 1, 2 or 3.")
        return play_rps()
    
    player = int(player_choice)

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
    
    print("\nPlay again?")
    
    while True:
        playagain = input("\nPlay again?\nY for Yes\nQ to Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else: 
            break
    
    if playagain.lower()=="y":
        return play_rps()
    else:
        print("\n🎉\n")
        print("Thank u for playing")
        sys.exit("Bye!")


play_rps()