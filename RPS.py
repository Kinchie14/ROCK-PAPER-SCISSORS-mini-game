import random



choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

print("Welcome to Rock Paper Scissors")

player = input("Please pick your choice Rock, Paper, Scissors?: ")

if player == computer:

    print("The computer chose",computer + " and you chose", player + ". The results are tie")

elif player == "Rock":
    if computer == "Paper":
        print("The computer chose",computer + " and you chose", player + ". The winner are the computer")
    if computer == "Scissors":
        print("The computer chose",computer + " and you chose", player + ". The winner are the player")
elif player == "Paper":
    if computer == "Rock":
        print("The computer chose",computer + " and you chose", player + ". The winner are the player")
    if computer == "Scissors":
        print("The computer chose",computer + " and you chose", player + ". The winner are the computer")
elif player == "Scissors":
    if computer == "Rock":
        print("The computer chose",computer + " and you chose", player + ". The winner are the computer")
    if computer == "Paper":
        print("The computer chose",computer + " and you chose", player + ". The winner are the player")