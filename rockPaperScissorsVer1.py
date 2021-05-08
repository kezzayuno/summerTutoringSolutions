import random

choiceWinDict = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}  # value is what they win against

computerChoice = random.choice(list(choiceWinDict.keys()))

choice = input("Pick Rock, Paper, or Scissors > ")
while choice.lower() not in choiceWinDict.keys():
    choice = input("That is not a choice!\nPick Rock, Paper, or Scissors > ")

if computerChoice == choice:
    print("It's a tie!")
elif choiceWinDict.get(choice) == computerChoice:
    print("You win! Computer chose {}".format(computerChoice))
else:  # choice's value was not the computer choice, then lose
    print("You lose! Computer chose {}".format(computerChoice))
