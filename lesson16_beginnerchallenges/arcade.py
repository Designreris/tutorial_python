# Game Selector Menu

import rps8
import guess_number
import sys
import argparse

def play_game(name='PlayerOne'):
  while True:
    player_choice = input(f'{name}, Please choose a game:\n 1 = Rock Paper Scissors\n 2 = Guess My Number\n x = Exit\n\n')

    if player_choice not in ['1','2','x']:
      print('Please enter 1,2 or x\n')
      continue

    if player_choice == "1":
      play_rps = rps8.rps(name)
      play_rps()
    elif player_choice == "2":
      play_guess_number = guess_number.guess_number_game(name)
      play_guess_number()
    else:
      sys.exit('Goodbye...\n')
if __name__ ==  '__main__':
  parser = argparse.ArgumentParser(
    description='Game Choice Menu'
  )

  parser.add_argument(
    '-n', '--name', metavar='name',
    help='Players name', required=False,
  )

  args = parser.parse_args()
  play_game(args.name)
