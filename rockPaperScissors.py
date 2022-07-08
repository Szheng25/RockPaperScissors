from random import randint

options = ["rock", "paper", "scissors"]

playerChoice = input("\nPick \"rock\", \"paper\", or \"scissors\": ")

computerChoice = options[randint(0, 2)]

print("\nRock 🪨, paper 📃, scissors ✂️, says shoot!\n")

if (playerChoice == computerChoice) : 
    print("It's a tie!")
elif (playerChoice == "rock") :
    if (computerChoice == "paper") :
        print("You lose! Paper 📃 covers rock 🪨.")
    elif (computerChoice == "scissors") :
        print("You win! Rock 🪨 crushes scissors ✂️.")
elif (playerChoice == "paper") :
    if (computerChoice == "scissors") :
        print("You lose! Scissors ✂️ cuts paper 📃.")
    elif (computerChoice == "rock") :
        print("You win! Paper 📃 covers rock 🪨.")
elif (playerChoice == "scissors") :
    if (computerChoice == "rock") :
        print("You lose! Rock 🪨 crushes scissors ✂️.")
    elif (computerChoice == "paper") :
        print("You win! Scissors ✂️ cuts paper 📃.")
