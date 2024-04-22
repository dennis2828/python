import sys
import random

def gn(name="Player1"):

    player_wins=0
    computer_wins=0

    def guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        player_choice = input(f"{name}, guess which number I'm thinking of... 1, 2 or 3.\n")
        
        if player_choice not in ["1","2","3"]:
            print(f"{name}, please enter 1, 2 or 3.")
            guess_number()
        
        player = int(player_choice)
        print(f"{name}, you chose {player}.")

        computer_choice = random.choice("123")
        computer = int(computer_choice)
        print(f"I was thinking about the number {computer}.\n")

        
        def player_win(player, computer):
            if player==computer: return True
            return False
        
        if player_win(player, computer):
            nonlocal player_wins

            player_wins+=1
            print(f"\n{name}, you win!")
        else:
            nonlocal computer_wins

            computer_wins+=1
            print(f"\nSorry, {name}. Better luck next time. 😢")

        print(f"\n{name}'s wins: {player_wins}\n")
        print(f"\nComputer's wins: {computer_wins}\n\n")

        while True:
            play_again = input(f"\nPlay again, {name}?\nY for Yes or\nN to Quit\n")

            if play_again.lower() not in ["y","n"]:
                continue
            break

        if(play_again.lower()=="y"):
            guess_number()
        else:
            print("\n🎉\n")
            print(f"Thank you for playing!\nBye {name}! 👏")
            sys.exit()
    
    return guess_number


if __name__=="__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name",metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    guess_number = gn(args.name)

    guess_number()