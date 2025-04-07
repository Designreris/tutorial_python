# FUNCTIONS
# naming conventions - lowercase with underscores
# Define function
def hello(): 
  print('Hello world!')

# Call function
# hello()

# Example
def sum(num1=0, num2=0): # argument = 0 - default value
  if (type(num1) is not int or type(num2) is not int):
    return # returns None - Same as null
  return num1 + num2

total = sum("a",3)
# print('Sum: ' + str(total))

# Function with multiple arguments
def multiple_items(*args): # * multiple parameters... - tuple
  print(args)
  print(type(args))

# multiple_items('Dave', 'john', 'sara')

def mult_named_items(**kwargs): # keyword arguments... - dictionary
  print(kwargs)
  print(type(kwargs))

mult_named_items(first='Dave', second='John', third='Sara')