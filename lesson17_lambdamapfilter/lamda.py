# LAMBDA FUNCTIONS
# AKA Anonymous Functions

squared = lambda num : num * num # anonymous function
# print(squared(2))

add_two = lambda num : num + 2
# print(add_two(12))

sum_total = lambda a, b : a + b
# print(sum_total(2,2))

def func_builder(x):
  return lambda num : num + x

add_ten = func_builder(10)
add_twenty = func_builder(20)

# print(add_ten(7))
# print(add_twenty(7))
#####################

# HIGHER ORDER FUNCTIONS
# Function returns a function.
# Function that take 1+ functions as param/args.
# Functions into Functions.

numbers = [3,7,12,18,20,21]

# Apply lambda function to list
squared_nums = map(lambda num : num * num, numbers)
# print(list(squared_nums))

# Filter example
odd_nums = filter(lambda num : num % 2 != 0, numbers)
# print(list(odd_nums))

# Reduce example
from functools import reduce

numbers = [1,2,3,4,5,1]
total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)
print(sum(numbers, 10))

names = ['Dave Gray', 'Sara Ito', 'John Jacob']
char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)
print(char_count)

