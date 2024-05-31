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


def display_results(score_percentage):
    """
    Display the results based on the score percentage.
    """
    print("**********************")
    print("****   RESULTS    ****")
    print("**********************")
    print(f" **Your score is: {score_percentage}% **")
    if score_percentage == 100:
        print("***** Perfect score! You are an 80's music legend! *****\n")
    elif score_percentage >= 80:
        print("***** Great job! You really know your 80's music! *****\n")
    elif score_percentage >= 50:
        print("***** Not bad, but you can do better. *****\n")
    elif score_percentage >= 20:
        print("***** Ah, you probably are a millennial... *****\n")
    else:
        print("***** Go and listen some Justin Bieber. *****\n")


def play_quiz():
    """
    Main function to play the quiz, the play_again method
    validates the user input in case it is not 'yes' or 'no'
    and make sure it's all lowercase.
    """
    questions = quiz_data.questions
    options = quiz_data.options
    answers = quiz_data.answers

    player_name = welcome_player()
    display_intro()

    play_again = "yes"
    while play_again.lower() == "yes":
        guesses = []
        score = 0
        questions, options, answers = get_random_questions(questions, options, answers)

        for question, opts, answer in zip(questions, options, answers):
            if ask_question(question, opts, answer):
                score =+ 1

        score_percentage = calculate_score(score, len(questions))
        display_results(score_percentage)

        play_again = input("Do you wanna go again? (yes/no):\n").lower()

# Run the quiz
play_quiz()
