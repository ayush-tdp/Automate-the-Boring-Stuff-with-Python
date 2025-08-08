import pyperclip
import re

rawData = pyperclip.paste()

if not rawData:
    print("No data found in clipboard.")
    exit()

def getAllEmails():
    """Extracts all email addresses from the raw data."""
    emailPattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    return re.findall(emailPattern, rawData)

def getAllPhoneNumbers():
    """Extracts all phone numbers from the raw data."""
    phonePattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(phonePattern, rawData)



emails = getAllEmails()
phone_numbers = getAllPhoneNumbers()
if not phone_numbers:
    print("No phone numbers found.")
else:
    print("Extracted Phone Numbers:")
    for number in phone_numbers:
        print(number)

print("-" * 20)

if not emails:
    print("No emails found.")
else:
    print("Extracted Emails:")
    for email in emails:
        print(email)
    pyperclip.copy('\n'.join(emails))

print("-" * 20)
