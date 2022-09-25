import random

user_wins = 0
computer_wins = 0
draw = 0

Choose = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Type q to quit: ").lower()
    if user_input == "q":

        if user_wins > computer_wins:
            print("User wins this game")
        else:
            print("Computer wins this game")
        print("user wins", user_wins, "times")
        print("computer wins", computer_wins, "times")
        print("Draw", draw)
        print("Goodbye! ")

        quit()
        break

    if user_input not in Choose:
        continue

    randomNumber = random.randint(0, 2)

    computer_Choose = Choose[randomNumber]
    print("computer picks", computer_Choose + '.')

    if user_input == computer_Choose:
        print("Its a draw ")
        draw += 1

    elif user_input == "rock" and computer_Choose == "scissor":
        print("You won")
        user_wins += 1

    elif user_input == "scissor" and computer_Choose == "paper":
        print("You won")
        user_wins += 1

    elif user_input == "paper" and computer_Choose == "rock":
        print("You won")
        user_wins += 1

    else:
        print("computer won ")
        computer_wins += 1

