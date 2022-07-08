from random import randint

options = ["rock", "paper", "scissors"]

playerChoice = input("\nPick \"rock\", \"paper\", or \"scissors\": ")

computerChoice = options[randint(0, 2)]

print("\nRock, paper, scissors, says shoot!\n")

if (playerChoice == computerChoice) : 
    print("It's a tie! You both picked " + playerChoice + ".")
elif (playerChoice == "rock") :
    if (computerChoice == "paper") :
        print("You lose! Paper covers rock. You chose " + playerChoice \
            + " but the computer chose " + computerChoice + ".")
    elif (computerChoice == "scissors") :
        print("You win! Rock crushes scissors. You chose " + playerChoice \
            + " and the computer chose " + computerChoice + ".")
            
# rock crushes scissors
# scissors cuts paper
# paper covers rock
print("\n")