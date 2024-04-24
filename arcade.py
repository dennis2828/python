import sys
import argparse
import guess_number 
import rps

def arcade(name):
    while True:
        choice = input(f"{name}, please enter 1, 2 or x\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\n Or press 'x' to exit the Arcade\n")

        if choice not in ["1", "2", "x"]:
            arcade(name)
        
        if choice=="1":
            rock_paper_scissors = rps.rps(name)
            rock_paper_scissors()
        elif choice=="2":
            gn = guess_number.gn(name)
            gn()
        else: sys.exit(f"\n\n See you next time!\n\Bye {name}!")



if __name__=="__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    arcade(args.name)