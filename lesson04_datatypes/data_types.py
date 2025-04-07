import math

# STRING DATA TYPE

# LITERAL ASSIGNMENT
first = 'Dave'
last = 'Gray'
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# CONSTRUCTOR FUNCTION
pizza = str('Pepperoni')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# CONCATENATION
fullname = first + ' ' + last
# print(fullname)
fullname += '!'
# print(fullname)

# CASTING A NUMBER TO A STRING
decade = str(1980)
# print(type(decade))
# print(decade)
statement = 'I like rock music from the ' + decade + 's.'
# print(statement)

# MULTIPLE LINES
multiline = '''
Hey, how are you?

I was just checking in.

            All good?

'''
# print(multiline)

# ESCAPING SPECIAL CHARACTERS \
sentence = 'I\'m back at work!\tHey!\n\n/Where\'s this at\\located?'
# print(sentence)

# STRING METHODS
# print(first)
# print(first.lower())
# print(first.upper())
# print(multiline.title())
# print(multiline.replace('good', 'ok'))

# print(len(multiline))
multiline += '                 '
multiline = '          ' + multiline
# print(len(multiline))
# print(len(multiline.strip()))
# print(len(multiline.lstrip())) # left side
# print(len(multiline.rstrip())) # right side

# BUILD A MENU EXAMPLE
title = 'menu'.upper()
# print(title.center(20, '='))
# print('Coffee'.ljust(16, '.') + '$1'.rjust(4))
# print('Muffin'.ljust(16, '.') + '$2'.rjust(4))
# print('Cheesecake'.ljust(16, '.') + '$4'.rjust(4))

# STRING INDEX VALUES
# print(first[1]) # index starts at 0
# print(first[-1]) # -1 last value
# print(first[1:-1]) # Range:
# print(first[1:]) # Range:

# SOME METHODS RETURN BOOLEAN DATA
# print(first.startswith('D'))
# print(first.endswith('Z'))

# BOOLEAN DATA TYPE
my_value = True
x = bool(False)
# print(type(x))
# print(isinstance(my_value, bool))

# NUMERIC DATA TYPES

# INTEGER TYPE
price = 100
best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

# FLOAT TYPE
gpa = 3.28
y = float(1.14)
# print(type(gpa))

# COMPLEX TYPE - ELECTRICAL ENGINEERING - J NOTATION
comp_value = 5+3j
# print(type(comp_value)) # complex
# print(comp_value.real)
# print(comp_value.imag)

# BUILT-IN FUNCTIONS FOR NUMBERS
# print(abs(gpa))
# print(abs(gpa * -1))
# print(round(gpa))
# print(round(gpa,1))

# MATH - REQUIRES import math
# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))

# CASTING A STRING TO A NUMBER
zipcode = '10001'
zip_value = int(zipcode) # casted to int
# print(type(zip_value))

# NOTE - Error if you attempt to cast incorrect data
# zip_value = int('new york') # Invalid literal for int()