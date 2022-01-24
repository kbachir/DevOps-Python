# For Loops

# Useful for doing things a set number of times or for doing things for every item in a collection

l = ['a', 'b', 'c']

# for letter in l:
#     print(letter)
#     print(letter.upper())

# for letter in l:
#     if letter == 'b':
#         print(letter.upper())
#     else:
#         print(letter)

# for i in range(10):
#     for letter in l:
#         print(i, letter)

me = {'name': 'Karim', 'age': 23, 'job': 'trainee'}

# for thing in me:
#     print(thing)  # this will print the keys by default
#
# for thing in me:
#     print(me[thing])  # this will print the values
#
# for thing in me.values():  # alternative for value printing
#     print(thing)

for key, value in me.items():
    print(key, value)

for key, value in me.items():
    if key == 'age':
        print(f"My {key} is {value} years old")
    else:
        print("Something else")


for thing in enumerate(l):
    print(thing)

for index in enumerate(l):
    print(f"{l} is in position {index}")

