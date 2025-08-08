str = "Hello, my email is example@gmail.com,ayush@gmail.com,piyush@nmail, alok@gmail.com"
import re
def match_pattern(text, pattern):
    return re.search(pattern, text) 
    # return re.search(pattern, text) is not None

pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
# print([match.group() for match in re.finditer(pattern, str)])
emails = re.compile(pattern)
print(emails.findall(str))  # Returns a list of all matches
# print(match_pattern(str, pattern))  # Returns the first match object or None 