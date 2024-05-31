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


questions = quiz_data.questions
options = quiz_data.options
answers = quiz_data.answers

def get_random_questions(questions, options, answers, num_questions=8):
    """
    Shuffles and get a specified number (8) of random questions
    from the quiz_data
    """
    combined_data = list(zip(questions, options, answers))
    random.shuffle(combined_data)
    questions, options, answers = zip(*combined_data)
    return questions [:num_questions], options[:num_questions], answers[:num_questions]


def ask_question(question, options, answer):
    """
    Ask a single question and return if the answer was correct.
    A while loop checks if the input is correct. If not
    then asks again until receives the correct input.
    """
    print("**********************\n")
    print(question)
    for option in options:
        print(option)
    while True:
        guess = input("What do you think? (a, b, c, d): ")
        if guess in ["a", "b", "c", "d"]:
            if guess == answer:
                print("YeeHaaw! Correct.\n")
                return True
            else:
                print("Nooope! Busted.")
                print(f"'{answer}' is the correct one. Dude, come on!!!\n")
                return False
        else:
            print("Invalid response. It's a, b, c or d. Watch your fingers!")


def calculate_score(score, num_questions):
    """
    Calculate the score percentage
    """
    return (score / num_questions) * 100


player_name = welcome_player()
display_intro()
