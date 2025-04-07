# ROCK PAPER SCISSOR GAME
import sys
import random
from enum import Enum

# Enum
class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

# print(RPS(1).name)
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

# Play again loop
play_again = True
while play_again:
  # Input
  player_choice = input('\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n')

  # Logic
  player = int(player_choice)
  if player < 1 or player > 3:
    sys.exit('You must enter 1,2, or 3.')

  computer_choice = random.choice('123')
  computer = int(computer_choice)

  # Output
  print('\nYou chose ' + str(RPS(player)).replace('RPS.', '') + '.') # with replace()
  print('Python chose ' + str(RPS(computer).name) + '.\n') # with .name

  if player == 1 and computer == 3:
    print('You Win!')
  elif player == 2 and computer == 1:
    print('You Win!')
  elif player == 3 and computer == 2:
    print('You Win!')
  elif player == computer:
    print('Tie Game!')
  else:
    print('Python Wins!')
  
  # Play again input
  play_again = input('\nPlay again? \nY for Yes or \nQ to Quit \n\n')
  if play_again.lower() == 'y':
    continue
  else:
    print('\nThanks for playing!\n')
    play_again = False # can use break instead
sys.exit('Goodbye...')


