from random import randint

options = ["rock", "paper", "scissors"]

playerChoice = input("\nPick \"rock\", \"paper\", or \"scissors\": ")

computerChoice = options[randint(0, 2)]

print("\nRock, paper, scissors, says shoot!\n")

