# ROCK PAPER SCISSOR GAME
import sys
import random
from enum import Enum

def rps():
  game_count = 0
  player_wins = 0
  python_wins = 0

  def play_rps():
    nonlocal player_wins
    nonlocal python_wins

    # Enum
    class RPS(Enum):
      ROCK = 1
      PAPER = 2
      SCISSORS = 3



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
    print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.") # with replace()
    print(f"Python chose {str(RPS(computer).name.title())}.\n") # with .name

    def decide_winner(player, computer):
      nonlocal player_wins
      nonlocal python_wins
      if player == 1 and computer == 3:
        player_wins += 1
        return 'You Win!'
      elif player == 2 and computer == 1:
        player_wins += 1
        return 'You Win!'
      elif player == 3 and computer == 2:
        player_wins += 1
        return 'You Win!'
      elif player == computer:
        return 'Tie Game!'
      else:
        python_wins += 1
        return 'Python Wins!'

    game_result = decide_winner(player, computer)
    print(game_result)

    nonlocal game_count
    game_count += 1
    print(f'\nGame count: { str(game_count)}')
    print(f'\nPlayer wins: { str(player_wins)}')
    print(f'\nPython wins: { str(python_wins)}')

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
  
  return play_rps

play = rps()

play()