# CLOSURES
# Closure is a function having access to the scope of its parent function after the parent function has returned.

# Example
def parent_function(person, coins):
  # coins = 3

  def play_game(): # access to parent function
    nonlocal coins # access to param coins, similar to var
    coins -= 1

    if coins > 1:
      print('\n' + person + ' has ' + str(coins) + ' coins left.')
    elif coins == 1:
      print('\n' + person + ' has ' + str(coins) + ' coin left.')
    else:
      print('\n' + person + ' is out of coins.')
  
  return play_game # closure

tommy = parent_function('Tommy', 3)
jenny = parent_function('Jenny', 5)

tommy()
tommy()
tommy()
jenny()