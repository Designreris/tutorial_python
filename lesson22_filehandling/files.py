# OS - for CWD
import os
# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
# print(current_working_directory)

# output will look something similar to this on a macOS system
# /Users/dionysialemonaki/Documents/my-projects/python-project
#####################################################################
# PATH - for CWD
from pathlib import Path

# get the current working directory
current_working_directory = Path.cwd()

# print output to the console
# print(current_working_directory)

# output will look something similar to this on a macOS system
# /Users/dionysialemonaki/Documents/my-projects/python-project
#####################################################################
# FILE HANDLING

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error  if it doesn't exist
f = open(f'{current_working_directory}\\names.txt', 'rt') 
# defaults 'r' for read
# print(f.read())
# print(f.read(4))
# print(f.readline()) # returns Dave
# print(f.readline()) # returns Jane

# Loop
# for line in f:
#   print(line)
# f.close() # NOTE: important to close file!

# Error Handler
# try:
#   f = open('name_list.txt')
#   print(f.read())
# except:
#   print('The file does not exist.')
# finally:
#   f.close()


# APPENDING - creates the file if it doesn't exist
# f = open('names.txt', 'a')
# f.write('Neil\n')
# f.close()

# f = open('names.txt')
# print(f.read())
# f.close()

# WRITE - overwrites file
f = open('context.txt', 'w')
f.write('I deleted all the context.')
f.close()

f = open('context.txt')
print(f.read())
f.close()

# NEW FILES
# Opens a file for writing, creates the file if it does not exist
f = open('name_list.txt', 'w')
f.close()

# Creates the specified, but returns an error if the file exists
if not os.path.exists('Dave.txt'):
  f = open('Dave.txt', 'x')
  f.close()

# Delete a file
# Avoid error if it does not exist
if os.path.exists('Dave.txt'):
  os.remove('dave.txt')
else:
  print('File does not exist.')

# EXAMPLE 
with open('more_names.txt') as f:
  content = f.read()

with open('names.txt', 'w') as f:
  f.write(content)