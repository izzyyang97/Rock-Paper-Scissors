#Rock Paper Scissors Game
#How is it played?
#Two People
#Three Choices: Rock, Paper, Scissors
#Rock beats Scissors
#Paper beats Rock
#Scissors beats Paper
#You tie if you have the same object

import random

over = False
wins = 0
losses = 0

while not over:
    choices = ['rock', 'scissors', 'paper']

    user_choice = input("Make your selection (rock, paper, scissors) - PLEASE TYPE IN LOWERCASE: ")
    if user_choice == 'quit':
        over = True
        continue
    print(f'You chose {user_choice}')

    computer_choice = random.choice(choices)
    print(f'The computer chose {computer_choice}')

    if user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
        print('Unacceptable choice. You must choose rock, paper, or scissors')
    elif user_choice == computer_choice:
        print('Tie! Play again!')
    elif user_choice == "rock" and computer_choice =="scissors":
        print('You win!')
        wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
        wins += 1
    else:
        print('You lose!')
        losses += 1

print(f'You won {wins} times and {losses} times')
