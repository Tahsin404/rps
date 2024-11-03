import random


class game:
    def input_data(self):
        options = ["Rock", "Paper", "Scissors"]
        while True:
            player_input = input("Please choose: Rock, Paper or Scissors? ").title()
            if player_input in options:
                break
            else:
                print(
                    "Please choose one of the following: Rock Paper or scissors".title()
                )

        computer_input = random.choice(options).capitalize()
        choices = {"player": player_input, "computer": computer_input}
        return choices

    def compute(self, player, computer):
        if player == computer:
            return "It is A Draw"
        elif player == "Rock":
            if computer == "Scissors":
                return "Rock Beats Scissors, You Win!"
            else:
                return "Paper Beats Rock, You lose"
        elif player == "paper".title():
            if computer == "rock".title():
                return "Paper Beats Rock, you win".title()
            else:
                return "Scissors cut paper, you lose".title()
        elif player == "Scissors".title():
            if computer == "paper".title():
                return "Scissors cut papers, you win!".title()
            else:
                return "Rock breaks Scissors, you lose!".title()


play = game()

while True:
    initiate = play.input_data()
    print(play.compute(initiate["player"], initiate["computer"]))

    while True:
        reinitialize = input("Would you like to play again?".title())

        if reinitialize == "Y":
            break
        elif reinitialize == "N":
            print("Thank You For Playing!")
            exit()
        else:
            print("Sorry didn't get you...")
