# password = input("Enter a password to check its strength: ")
password = "Example@Password123"
def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in password):
        return "Weak: Password must contain at least one special character."
    return "Strong: Password meets all requirements."

result = check_password_strength(password)
print(result)

# do using re 

import re
def check_password_strength_regex(password):
    """Check password strength using regular expressions."""
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search(r'\d', password):
        return "Weak: Password must contain at least one digit."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain at least one lowercase letter."
    if not re.search(r'[!@#$%^&*()\-_+=\[\]{}|;:\'",.<>?]', password):
        return "Weak: Password must contain at least one special character."
    return "Strong: Password meets all requirements."
result_regex = check_password_strength_regex(password)
print(result_regex)