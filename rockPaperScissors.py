from random import randint

options = ["rock", "paper", "scissors"]

playerChoice = input("\nPick \"rock\", \"paper\", or \"scissors\": ")
while (playerChoice not in options) :
    playerChoice = input("\nNot a valid choice! Please pick from \"rock\", \"paper\", or \"scissors\": ")

computerChoice = options[randint(0, 2)]

print("\nRock, paper, scissors, says shoot!\n")

if (playerChoice == computerChoice) : 
    print("It's a tie!")
elif (playerChoice == "rock") :
    if (computerChoice == "paper") :
        print("You lose! Paper covers rock.\n")
    else:
        print("You win! Rock crushes scissors.\n")
elif (playerChoice == "paper") :
    if (computerChoice == "scissors") :
        print("You lose! Scissors cuts paper.\n")
    else:
        print("You win! Paper covers rock.\n")
else:
    if (computerChoice == "rock") :
        print("You lose! Rock crushes scissors.\n")
    else:
        print("You win! Scissors cuts paper.\n")
