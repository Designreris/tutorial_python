# PYTHON MODULES - LIBRARIES

# MATH MODULE
import math
# print(math.pi)

# SYS MODULE
import sys

# RANDOM MODULE
import random as rdm
# print(dir(rdm))

# for item in dir(rdm):
#   print(item)

# ENUM MODULE
from enum import Enum

#NOTE: You can import other py files as modules!
# import rps6 #NOTE: runs rps6 game on import!
import example
# example.module_example()

# NAME MODULE
print(__name__) # __main__
print(example.__name__) # example

if __name__ == "__main__":
  example.module_example()


# ROCK PAPER SCISSORS GAME
from rps7 import rock_paper_scissors

# rock_paper_scissors()

