# ROCK PAPER SCISSOR GAME
import sys
import random
from enum import Enum

game_count = 0

def play_rps():
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

  # Input
  player_choice = input('\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n')
  if player_choice not in ['1','2','3']:
    print('You must enter 1, 2, or 3.')
    return play_rps()

  # Logic
  player = int(player_choice)
  if player < 1 or player > 3:
    sys.exit('You must enter 1,2, or 3.')

  computer_choice = random.choice('123')
  computer = int(computer_choice)

  # Output
  print('\nYou chose ' + str(RPS(player)).replace('RPS.', '') + '.') # with replace()
  print('Python chose ' + str(RPS(computer).name) + '.\n') # with .name

  def decide_winner(player, computer):
    if player == 1 and computer == 3:
      return 'You Win!'
    elif player == 2 and computer == 1:
      return 'You Win!'
    elif player == 3 and computer == 2:
      return 'You Win!'
    elif player == computer:
      return 'Tie Game!'
    else:
      return 'Python Wins!'

  game_result = decide_winner(player, computer)
  print(game_result)

  global game_count
  game_count += 1
  print('\nGame count: ' + str(game_count))

  # Play again input
  print('\nPlay again?')
  while True:
    play_again = input( '\nY for Yes or \nQ to Quit\n')
    if play_again.lower() not in ['y','q']:
      continue # starts loop again
    else:
      break
  if play_again.lower() == 'y':
    return play_rps()
  else:
    print('\nThanks for playing!\n')
    sys.exit('Goodbye...')


play_rps()