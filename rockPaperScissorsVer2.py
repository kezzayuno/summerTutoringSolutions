import random

choices = ['rock', 'paper', 'scissors']
computerChoice = random.choice(choices)


choice = input("Pick Rock, Paper, or Scissors > ")
while choice.lower() not in choices:
    choice = input("That is not a choice!\nPick Rock, Paper, or Scissors > ")

if computerChoice == choice:  # if user and computer pick the same action
    print("It's a tie!")
elif computerChoice == 'rock' and choice == 'paper' or computerChoice == 'paper' and choice == 'rock':
    if choice == 'rock':
        print("You lose! Computer chose paper!")
    else:  # choice == 'paper'
        print("You win! Computer chose rock!")
elif computerChoice == 'paper' and choice == 'scissors' or computerChoice == 'scissors' and choice == 'paper':
    if choice == 'paper':
        print("You lose! Computer chose scissors!")
    else:  # choice == 'scissors'
        print("You win! Computer chose paper!")
elif computerChoice == 'rock' and choice == 'scissors' or computerChoice == 'scissors' and choice == 'rock':
    if choice == 'scissors':
        print("You lose! Computer chose rock!")
    else:  # choice == 'rock'
        print("You win! Computer chose scissors!")