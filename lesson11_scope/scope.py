# SCOPES
name = 'Dave' # Global Scope
count = 1

def greeting(first_name): # Global Scope Function
  color = 'blue' # Local Scope
  print(color) # From Local Scope
  print(name) # From Global Scope
  print(first_name) # From Parameter

# print(color) # not defined, in local function
# greeting('John')

def another(): # Global Scope Function
  greeting('Sara') # From Function Global Scope

# another()


# FUNCTION DEFINED WITHIN FUNCTION EXAMPLE
def another_2(): # Global Scope Function
  color = 'pink'
  
  # count = 2 # another variable not global!, cant modify.
  global count # Global keyword, gives access to global variable
  count += 2 # Modify Global Variable
  print(count)

  def greeting_2(first_name): # Nested Local Scope Function
    nonlocal color # color from parent
    color = 'red'

    print(color) # From Parent Function
    print(name) # From Global Scope
    print(first_name) # From Parameter

  greeting_2('Matt') # Local Scope Function

another_2()
# greeting_2('Test') # No Access To Nested Function 

# NOTE: POLLUTING THE GLOBAL SCOPE - Try to keep as few functions/variables in the Global Scope as possible to avoid convolution and maintain clarity!

