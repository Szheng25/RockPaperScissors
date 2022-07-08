from random import randint

options = ["rock", "paper", "scissors"]

playerChoice = input("\nPick \"rock\", \"paper\", or \"scissors\": ")

computerChoice = options[randint(0, 2)]

print("\nRock 🪨, paper 📃, scissors ✂️, says shoot!\n")

if (playerChoice == computerChoice) : 
    print("It's a tie! You both picked " + playerChoice + ".\n")
elif (playerChoice == "rock") :
    if (computerChoice == "paper") :
        print("You lose! Paper 📃 covers rock 🪨. You chose " + playerChoice \
            + " but the computer chose " + computerChoice + ".\n")
    elif (computerChoice == "scissors") :
        print("You win! Rock 🪨 crushes scissors ✂️. You chose " + playerChoice \
            + " and the computer chose " + computerChoice + ".\n")
elif (playerChoice == "paper") :
    if (computerChoice == "scissors") :
        print("You lose! Scissors ✂️ cuts paper 📃. You chose " + playerChoice \
            + " but the computer chose " + computerChoice + ".\n")
    elif (computerChoice == "rock") :
        print("You win! Paper 📃 covers rock 🪨. You chose " + playerChoice \
            + " and the computer chose " + computerChoice + ".\n")
elif (playerChoice == "scissors") :
    if (computerChoice == "rock") :
        print("You lose! Rock 🪨 crushes scissors ✂️. You chose " + playerChoice \
            + " but the computer chose " + computerChoice + ".\n")
    elif (computerChoice == "paper") :
        print("You win! Scissors ✂️ cuts paper 📃. You chose " + playerChoice \
            + " and the computer chose " + computerChoice + ".\n")
