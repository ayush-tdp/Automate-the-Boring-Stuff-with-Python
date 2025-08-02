passwordFile = open('password.txt')
password = passwordFile.read()
print("Enter Password:-")
userPassword = input()
if password == userPassword:
    print("Access Approved")
    if userPassword == "1234":
        print("Chutiya hai kya? Itna easy password kaun rakhta hai!")
else:
    print("Access Denied")