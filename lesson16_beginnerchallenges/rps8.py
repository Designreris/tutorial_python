# ROCK PAPER SCISSOR GAME
import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
  game_count = 0
  player_wins = 0
  python_wins = 0

  def play_rps():
    nonlocal name
    nonlocal player_wins
    nonlocal python_wins

    # Enum
    class RPS(Enum):
      ROCK = 1
      PAPER = 2
      SCISSORS = 3



    # Play again loop
    # Input
    player_choice = input(f'\n{name}, please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n')
    if player_choice not in ['1','2','3']:
      print('You must enter 1, 2, or 3.')
      return play_rps()

    # Logic
    player = int(player_choice)
    if player < 1 or player > 3:
      sys.exit(f'{name}, please must enter 1,2, or 3.')

    computer_choice = random.choice('123')
    computer = int(computer_choice)

    # Output
    print(f"\n{name} chose {str(RPS(player)).replace('RPS.', '').title()}.") # with replace()
    print(f"Python chose {str(RPS(computer).name.title())}.\n") # with .name

    def decide_winner(player, computer):
      nonlocal name
      nonlocal player_wins
      nonlocal python_wins
      if player == 1 and computer == 3:
        player_wins += 1
        return f'{name}, you win!'
      elif player == 2 and computer == 1:
        player_wins += 1
        return f'{name}, you win!'
      elif player == 3 and computer == 2:
        player_wins += 1
        return f'{name}, you win!'
      elif player == computer:
        return 'Tie Game!'
      else:
        python_wins += 1
        return f'Python Wins!\nSorry, {name}...😢'

    game_result = decide_winner(player, computer)
    print(game_result)

    nonlocal game_count
    game_count += 1
    print(f'\nGame count: {game_count}')
    print(f'{name}\'s wins: {player_wins}')
    print(f'Python wins: {python_wins}')

    # Play again input
    print(f'\nPlay again?, {name}?')
    while True:
      play_again = input( 'Y for Yes or \nQ to Quit\n')
      if play_again.lower() not in ['y','q']:
        continue # starts loop again
      else:
        break
    if play_again.lower() == 'y':
      return play_rps()
    else:
      print('\nThanks for playing!\n')
      if __name__ == '__main__':
        sys.exit(f'Goodbye {name}!')
      else:
        return
  
  return play_rps


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(
    description='Provides a personalized game experience'
  )

  parser.add_argument(
    '-n', '--name', metavar='name',
    required=True, help='The name of the person playing the game.'
  )

  args = parser.parse_args()

  rock_paper_scissors = rps(args.name)
  rock_paper_scissors()