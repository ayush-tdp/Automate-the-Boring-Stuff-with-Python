name=""
count=0

while name != "Ayush":
    if count == 5:
        print("Maximum try exceed! Please try again after some time.")
        break
    count += 1
    if name != "":
        print(f"Invalid Name:- {name}")
    name = input("Enter your name:- ")

if name == "Ayush":
    print(f"Thank you! {name}")