# # Multiline Strings with triple Quotes
# print('''Dear Alice,
# Eve's cat has been arrested for catnapping, cat burglary, and extortion.
# Sincerely,
# Bob''')
# print()
# print('Dear Alice,\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\nSincerely,\nBob')
# print()

# # Multiline Comments

# """This is a test Python program.
# Written by Al Sweigart al@inventwithpython.com
# This program was designed for Python 3, not Python 2.
# """
# def spam():
#     """This is a multiline comment to help
#     explain what the spam() function does."""
#     print('Hello!')

# spam()

# # Indexing and Slicing Strings
# spam = 'Hello, world!'
# print(spam[0])
# print(spam[1])
# print(spam[2])
# print(spam[-1])
# print(spam[0:5])
# print(spam[:6])
# print(spam[7:])

# # The in and not in Operators with Strings

# print('Hello' in 'Hello, world!')
# print('Hello' not in 'Hello, world!')
# print('cat' in 'My cat is fat.')
# print('cat' not in 'My dog is fat.')

# # Cases 

# print("Hello".lower())
# print("Hello".upper())
# print("HELLO".isupper())
# print("hello".islower())


# # The isX String Methods

# print('hello'.isalpha())
# print('hello123'.isalpha())
# print('hello123'.isalnum())
# print('hello'.isalnum())
# print('123'.isdecimal())
# print(' '.isspace())
# print('This Is Title Case'.istitle())
# print('This Is Title Case 123'.istitle())
# print('This Is not Title Case'.istitle())
# print('This Is NOT Title Case Either'.istitle())

# # The startswith() and endswith() String Methods

# print('Hello, world!'.startswith('Hello'))
# print('Hello, world!'.endswith('world!'))
# print('Hello, world!'.startswith('world!'))
# print('Hello, world!'.endswith('Hello'))

# # The join() and split() String Methods

# print(', '.join(['cats', 'rats', 'bats']))
# print(' '.join(['My', 'name', 'is', 'Simon']))  
# print('My name is Simon'.split())
# print('My name is Simon'.split(' '))
# print('My name is Simon'.split('m'))
# print('My name is Simon'.split('z'))  # No 'z' in the string, so it returns the whole string in a list

# # Justifying Text with rjust(), ljust(), and center()

# print('Hello'.rjust(20,"-"))
# print('Hello'.center(20,"-"))
# print('Hello'.ljust(20,"-"))

# Removing Whitespace with strip(), rstrip(), and lstrip()

# print('   Hello, world!   '.strip())
# print('   Hello, world!   '.rstrip())
# print('   Hello, world!   '.lstrip())

# Copying and Pasting Strings with the pyperclip Module

import pyperclip
pyperclip.copy('Hello Ayush!')
print(pyperclip.paste())  # This will print 'Hello Ayush!' from the clipboard