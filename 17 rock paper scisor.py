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