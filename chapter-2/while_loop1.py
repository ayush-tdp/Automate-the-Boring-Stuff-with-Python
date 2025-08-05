while True:
    print("What is your name?")
    name = input()
    if name != "Ayush":
        continue
    print(f"Hello {name}! What is your password?")
    password = input()
    if password == "ayush":
        break
print("Access Granted")