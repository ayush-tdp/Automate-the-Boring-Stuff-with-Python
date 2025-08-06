# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)

#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')


spam = {'color': 'red', 'age': 42}
# for v in spam.keys():
#     print(v)
for (k,v) in spam.items():
    print(k,v)
# for v in spam.values():
#     print(v)
print("age" in spam.keys())