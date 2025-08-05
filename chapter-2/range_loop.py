names = {}

for i in range(2,15,2):
    tempName = input(f"Enter your {i} name:- ")
    names.update({i:tempName})
print(names)
for i in names:
    print(f"Your name is {i}:{names[i]}")

