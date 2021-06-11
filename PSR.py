# This is an import statement which can allow the program to use random items from a particular list (in this case)
import random
possible_choices = ["rock", "paper", "scissors"]
# this is the a code for counting the score for the user
score = 0
again = "yes"
# These are the set of rules that checks user input and computer random choice and then prints out the appropriate answer.
while again.lower() == 'yes' or again.lower() == 'y':
    user_choice = input("Enter a choice (rock, paper, scissors)(r,s,p)")
    computer_choice = random.choice(possible_choices)
    if user_choice == computer_choice:
        print("It's a Tie!")

    elif user_choice == "rock" or user_choice == "r":
        if computer_choice == "scissors":
            score = score + 1
            print("Rock Smashes Scissors! You WIN!, Current Score: ", score)
        else:
            print("Paper covers rock! You LOSE! Current score: ", score)

    elif user_choice == "paper" or user_choice == "p":
        if computer_choice == "rock":
            score = score + 1
            print("Paper covers Rock! You WIN!, Current Score: ", score)
        else:
            print("Scissors cuts paper! You LOSE! Current score: ", score)

    elif user_choice == "scissors" or user_choice == "s":
        if computer_choice == "paper":
            score = score + 1
            print("Scissors cuts paper! You WIN!. Current score: ", score)
        else:
            print("Rock smashes scissors! You LOSE!")
    #This is a try again code which will come up when a person doesn't enter r, s, p / rock, paper, scissors
    else:
        print("Error Please Try Again.")
    if user_choice == "r" or user_choice == "s" or user_choice == "r":
        # This is a code for asking the user if they want to play again.
        again = input("Would you like to continue? (y,n)")
