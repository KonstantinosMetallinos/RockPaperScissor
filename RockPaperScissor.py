import random

# ======== Private static final variables. ========
printing_choices = ["Paper", "Rock", "Scissor"]
choices = ["p", "r", "s"]
# ======== Private static final variables. ========


def print_sarcastic_statement():
    print("So... I am sure if you explain your mental (in)capabilities to an adult, schools may make an exception "
          "and allow you back in :)")
    print("A *NUMBER* of games can only be a *Number*. If this is hard for you to comprehend, maybe you shouldn't be "
          "allowed on a computer... \nBoth for your and humanities well-being. \nLets try this again...")


def check_user_input(input_to_check):
    global choices
    while input_to_check not in choices:
        input_to_check = input("Listen here you little shit, its simple, type p, r or s. Stop being a smart ass!")
    return input_to_check


def get_number_of_games():
    while True:
        user_input_number_of_games = input("How many number of games would you like to play?")
        try:
            user_input_number_of_games = int(user_input_number_of_games)
            if user_input_number_of_games < 0:  # if not a positive int print message and ask for input again
                print("<sarcasm>Haha funny mate, lets play negative number of games eh? haha hilarious!<sarcasm/>")
                continue
            elif user_input_number_of_games == 0:
                print("Haha funny guy eh? 0 games eh? We are done here.")
                exit()
            return user_input_number_of_games
        except ValueError:
            print_sarcastic_statement()


def play_one_round(human_wins, computer_wins):
    # Allow for round decisions
    user_input = check_user_input(input("Pick r (Rock), p (Paper) or s (Scissor)"))
    user_input_numeric = choices.index(user_input)
    computer_input_numeric = random.randint(0, 2)

    # Unnecessary - used to stay within PEP8 char per line limit.
    printable_user = printing_choices[user_input_numeric]
    printable_computer = printing_choices[computer_input_numeric]

    if computer_input_numeric == user_input_numeric:
        print("Its a draw! You both chose: ", printing_choices[user_input_numeric])
    elif user_input_numeric == ((computer_input_numeric + 1) % 3):
        print("")
        print("Get Reckt mate, PC power! Woop woop!", printable_computer, "beats", printable_user)
        computer_wins += 1
    elif computer_input_numeric == ((user_input_numeric + 1) % 3):
        print("You got lucky this time punk.", printable_user, "beats", printable_computer)
        human_wins += 1
    else:
        print("How did we even get here? Reach out to the developer who wrote this and give them the below info:")
        print("User entered: ", user_input)
        print("Computer chose: ", computer_input_numeric)

    return human_wins, computer_wins


if __name__ == "__main__":
    number_of_games = get_number_of_games()
    print("Player chose to play", number_of_games, "game(s)")
    print("Good Luck and Have Fun!")

    num_of_human_wins = 0
    num_of_computer_wins = 0

    for game_round in range(int(number_of_games)):
        print("===== Round", game_round+1, "=====")
        num_of_human_wins, num_of_computer_wins = play_one_round(num_of_human_wins, num_of_computer_wins)

    print("\n\nAnd the winner is....")
    if num_of_human_wins == num_of_computer_wins:
        print("Its a tie! Wow you can't even beat a computer... how sad.")
    elif num_of_human_wins > num_of_computer_wins:
        print("Wow... eh.... must have been a counting error... Looks like its you... this game is rigged man.")
    else:
        print("I mean... was this even ever a question? Clearly not you. But you are probably used to that by now.")
