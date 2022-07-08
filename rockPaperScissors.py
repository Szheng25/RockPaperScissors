from random import randint

options = ["rock", "paper", "scissors"]

player = input("\nPick \"rock\", \"paper\", or \"scissors\": ")

while (player not in options) :
    player = input("\nNot a valid choice! Please pick from \"rock\", \"paper\", or \"scissors\": ")

computer = options[randint(0, 2)]

print("\nRock, paper, scissors, says shoot!\n")

if (player == computer) : 
    print("It's a tie!\n")
elif (player == "rock") :
    if (computer == "paper") :
        print("You lose, " + computer + " covers " + player + ".\n")
    else:
        print("You win, " + player + " crushes " + computer + ".\n")
elif (player == "paper") :
    if (computer == "scissors") :
        print("You lose, " + computer + " cuts " + player + ".\n")
    else:
        print("You win, " + player + " covers " + computer + ".\n")
else:
    if (computer == "rock") :
        print("You lose, " + computer + " crushes " + player + ".\n")
    else:
        print("You win, " + player + " cuts " + computer + ".\n")
