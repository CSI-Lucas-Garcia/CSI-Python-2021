import random
print("Lets play rock, paper, scissors!")
Rps = ["rock, paper, scissors"]

playerChoice = input("Choose one: rock, paper, scissors\n")

foo = ['rock', 'paper', 'scissors']
computerChoice = random.choice(foo)
print(f"Computer selected: {computerChoice}")
print(f"Player selected: {playerChoice}")


if(playerChoice == computerChoice):
    print("You tied, try again")
elif(playerChoice == "rock" and computerChoice == "paper"):
    print("Paper beats rock, you lost")
elif(playerChoice == "paper" and computerChoice == "rock"):
    print("You won, paper beats rock")
elif(playerChoice == "rock" and computerChoice == "scissors"):
    print("You won, paper crushes the scissors")
elif(playerChoice == "scissors" and computerChoice == "paper"):
    print("You won, the scissors cut the paper")
elif(playerChoice == "paper" and computerChoice == "scissors"):
    print("You lost, scissors cut paper")
elif(playerChoice == "scissors" and computerChoice == "rock"):
    print("You lost, the rock crushed your scissors")

else:
    print("Something is not right, try again")

