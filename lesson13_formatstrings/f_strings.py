# ADVANCED STRING FORMATTING
 
person = 'Dave'
coins = 3

# STANDARD METHOD
# print('\n' + ' has' + str(coins) + ' coins left.')

###########################
# %s METHOD
message = '\n %s has %s coins left.' % (person, coins)
# print(message)

# FORMAT METHOD - OLD CONVENTION
############################
message = '\n {} has {} coins left.'.format(person, coins)
# print(message)

message = '\n {1} has {0} coins left.'.format(coins, person)
# print(message)

message = '\n {person} has {coins} coins left.'.format(
  coins=coins, person=person
)
# print(message)

player = { 'person': 'Dave', 'coins': 3 }

message = '\n {person} has {coins} coins left.'.format(**player) # **kwargs
# print(message)

############################
# F_STRING METHOD - PREFERRED 

message = f'\n{person} has {coins} left.'
# print(message)

message = f'\n{person.lower()} has {2 * 5} left.'
# print(message)

message = f"\n{player['person']} has {player['coins']} left."
print(message)

# F_STRING OPTIONS :
num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}")

# for num in range(1,11):
#   print(f"\n2.25 times {num} is {2.25 * num:.2f}")

# for num in range(1,11):
#   print(f"{num} divided by 4.52 is {num / 4.52:.2%}")