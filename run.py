import random
import quiz_data

def welcome_player():
    """
    Ask for player's name and welcome them.
    Also make sure the name is at least 3 characters long.
    """
    while True:
        player_name = input("What's your name:\n")
        if len(player_name) >= 3:
            print(f"\nWelcome, {player_name}! Let's get it on.\n")
            return player_name
        else:
            print("Minimum of 3 characters please and no foul words!")


def display_intro():
    """
    Display game introduction
    """
    print("  ******************************************")
    print(" *                                          *")
    print("*       Welcome to the 80's Music Quiz       *")
    print(" *                                          *")
    print("  ******************************************")
    print("    Let's see how well you know 80's music!\n")

player_name = welcome_player()
display_intro()
