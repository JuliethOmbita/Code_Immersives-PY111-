import random

# This funtion verify the user imput:
# - If the input is valid: Assing a numerical valio to the string input.
# - If the input is invalid: Let the user know and set a False flag.


def valInput(usInput):
    if usInput.lower() == "rock":
        print("it's rock")
        return 0
    elif usInput.lower() == "paper":
        return 1
    elif usInput.lower() == "scissor":
        return 2
    else:
        print("Imput invalid. Let's try again... \v")
        return 3


def rpsGame():
    print("The rock paper scissor rules are the followings: \n"
          "\t - Rock vs paper -> Paper wins \n"
          "\t - Rock vs scissor -> Rock wins \n"
          "\t - Paper vs scissor -> Scissor wins \n")

    usInput = (input("Enter a option between Rock, Paper or Scissor: "))
    usSol = valInput(usInput)

    if usSol != 3:
        print("\v\t...Rock Paper Scissor set go...\v")
        # Randint provides a random number between 0 and 2, which is the computer solution.
        compSol = random.randint(0, 2)
        # This if statement is printing out the computer solution in user words:rock, paper or scissor
        if compSol == 0:
            print(f"The computer solution: Rock.\v")
        elif compSol == 1:
            print(f"The computer solution: Paper.\v")
        else:
            print(f"The computer solution: Scissor.\v")

        # Comparison between the user solution and computer solution
        winner = False  # Inicialize the winner variable w a random value.
        if usSol == compSol:
            print("It's a tie.")
        elif (usSol == 0 and compSol == 1) or (usSol == 1 and compSol == 0):
            winner = 1
            print("Paper cover rock. Paper wins.")
        elif (usSol == 0 and compSol == 2) or (usSol == 2 and compSol == 0):
            winner = 0
            print("Rock destroy scissor. Rock wins.")
        elif (usSol == 1 and compSol == 2) or (usSol == 2 and compSol == 1):
            winner = 2
            print("Scissor cuts paper. Scissor wins.")

        # Printing either user or computer wins
        if usSol == winner:
            print("You win!!!\v")
        elif compSol == winner:
            print("Computer win!!!\v")
        else:
            print("No winners, no losers.\v")
    else:
        rpsGame()


rpsGame()
