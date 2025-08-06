# Practice Questions

# 1. What does the code for an empty dictionary look like?
# -> spam = {}
# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
# -> spam = {'foo': 42}
# 3. What is the main difference between a dictionary and a list?
# -> Dictionaries are unordered collections of key-value pairs, while lists are ordered collections of items.
# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# -> KeyError: 'foo'

# 5. If a dictionary is stored in spam, what is the difference between the
# expressions 'cat' in spam and 'cat' in spam.keys()?
# -> No difference, both check if 'cat' is a key in the dictionary.

# 6. If a dictionary is stored in spam, what is the difference between the
# expressions 'cat' in spam and 'cat' in spam.values()?
# -> 'cat' in spam checks if 'cat' is a key, while 'cat' in spam.values() checks if 'cat' is a value.

# 7. What is a shortcut for the following code?
# if 'color' not in spam:
# spam['color'] = 'black'
# -> spam.setdefault('color', 'black')

# 8. What module and function can be used to “pretty print” dictionary
# values?
# -> pprint.pprint()