import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scisor"]
    user_input = input("Chose rock, paper, or scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended")
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is a rock")
            print("Computer input is a rock")
            print("It is a tie")

        elif computer_input == "paper":
            print("Your input is a rock")
            print("Computer input is a paper")
            print("You lose")
            computer_points += 1

        elif computer_input == "scissor":
            print("Your input is a rock")
            print("Computer input is a scissor")
            print("You win")
            user_points += 1