# BEGINNER CHALLENGE - GUESS NUMBER GAME
import sys
import random

def guess_number_game(name='PlayerOne'):
  game_count = 0
  player_wins = 0
  python_wins = 0

  def play_guess_number_game():
    nonlocal name
    nonlocal player_wins
    nonlocal python_wins

    # Player Input
    player_choice = input(f"{name}, guess which number I'm thinking of... 1, 2, or 3.\n")
    if player_choice not in ['1', '2', '3']:
      print('Please enter 1,2 or 3.\n') 
      return play_guess_number_game()

    # Logic
    player = int(player_choice)
    if player < 1 or player > 3:
      sys.exit(f"{name}, you must enter a number between 1-3.")

    computer_choice = int(random.choice(['1','2','3']))

    print(f"{name} chose {player_choice}\nPython chose {str(computer_choice)}.")

    def decide_winner(player, computer_choice):
      nonlocal name
      nonlocal player_wins
      nonlocal python_wins

      if player == computer_choice:
        player_wins += 1
        return(f"{name}, you Win!")
      else:
        python_wins += 1
        return(f"{name}, you Lose!")

    game_result = decide_winner(player, computer_choice)
    print(game_result)

    nonlocal game_count
    game_count += 1
    print(f"Game Count: {game_count}")
    print(f"{name} Wins: {player_wins}")
    print(f"Python Wins: {python_wins}")

    # Play Again
    print(f"\n{name}, play again? ...")
    while True:
      play_again = input(f"\n{name}, Y to play again\n, Q to quit\n")
      if play_again.lower() not in ['y','q']:
        continue
      else:
        break
    
    if play_again.lower() == 'y':
      return play_guess_number_game()
    else:
      print('Thanks for playing\n')
      if __name__ == '__main__':
        sys.exit(f'goodbye {name}')
      else:
        return

  return play_guess_number_game
  
if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(
    description='A number guessing game input'
  )

  parser.add_argument(
    '-n','--name', metavar='name',
    required=True,
    help='The players name for the game.'
  )

  args = parser.parse_args()

  guess_number_game(args.name)



