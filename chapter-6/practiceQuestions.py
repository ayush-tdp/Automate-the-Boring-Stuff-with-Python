# Practice Questions

# 1. What are escape characters?
# -> Escape characters are special characters in strings that allow you to include characters that are otherwise difficult to type, such as newlines or tabs.

# 2. What do the \n and \t escape characters represent?
# -> \n represents a newline character, while \t represents a tab character.
    
# 3. How can you put a \ backslash character in a string?
# -> You can put a backslash in a string by escaping it with another backslash: \\

# 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it
# a problem that the single quote character in the word Howl's isn’t
# escaped?
# -> The single quote in Howl's is inside double quotes, so it doesn't need to be escaped.

# 5. If you don’t want to put \n in your string, how can you write a string
# with newlines in it?
# -> You can use triple quotes to create a multi-line string.

# 6. What do the following expressions evaluate to?
# • 'Hello world!'[1] -> 'e'
# • 'Hello world!'[0:5] -> 'Hello'
# • 'Hello world!'[:5] -> 'Hello'
# • 'Hello world!'[3:] -> 'lo world!'

# 7. What do the following expressions evaluate to?
# • 'Hello'.upper() -> 'HELLO'
# • 'Hello'.upper().isupper() -> True
# • 'Hello'.upper().lower() -> 'hello'

# 8. What do the following expressions evaluate to?
# • 'Remember, remember, the fifth of November.'.split() -> ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
# • '-'.join('There can be only one.'.split()) -> 'There-can-be-only-one.'

# 9. What string methods can you use to right-justify, left-justify, and center
# a string?
# -> You can use rjust(), ljust(), and center() methods to right-justify, left-justify, and center a string, respectively.

# 10. How can you trim whitespace characters from the beginning or end of
# a string?
# -> You can use the strip() method to remove whitespace characters from the beginning and end of a string.