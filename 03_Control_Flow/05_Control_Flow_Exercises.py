print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:

#for i in range(x):
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:

for item in x:
    if item % 2 == 0:
        print(item)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:

for item in x[0:5]:
    if item % 2 == 0:
        print(item)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

new_list = []
for initial in names:
    new_list.append(initial[:1])

print(new_list)


print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:

new_list2 = []
for space in names:
    new_list2.append(space.index(" "))
print(new_list2)



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

new_list3 = []

for name in names:

    initial = name.split()

    firstName = initial[0][0]
    lastName = initial[1][0]
    full_initials = firstName + lastName

    new_list3.append(full_initials)

print(new_list3)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates

list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

# Correct function but inefficient code. Whenever there is repetition, find out how to use a loop. Use below example for reference #

# for x in list_of_lists:
#
#     new_set_1 = set(list_of_lists[0])
#     new_set_2 = set(list_of_lists[1])
#     new_set_3 = set(list_of_lists[2])
#     new_set_4 = set(list_of_lists[3])
#
# if len(new_set_1) == len(list_of_lists[0]):
#     print(list_of_lists[0])
# else:
#     print("Fail")
#
# if len(new_set_2) == len(list_of_lists[1]):
#     print(list_of_lists[1])
# else:
#     print("Fail")
#
# if len(new_set_3) == len(list_of_lists[2]):
#     print(list_of_lists[2])
# else:
#     print("Fail")
#
# if len(new_set_4) == len(list_of_lists[3]):
#     print(list_of_lists[3])
# else:
#     print("Fail")

for list in list_of_lists:

    test = set(list)

    if len(test) == len(list):
        print(list)

# # -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

# prompt = True
#
# while prompt:
#
#     user_input = input("Enter a number greater than 100.\n")
#
#     if user_input.isdigit():
#         if int(user_input) > 100:
#             print(f"You chose the number {user_input}.")
#         else:
#             print("Please try again.\n")
#     else:
#         print("Please ensure you are entering a number.")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

# prompt = True
# while prompt:
#
#     user_input = input("Enter a number greater than 100.\n")
#     prime = True
#     prime = int(user_input) % x == 0
#
#     if user_input.isdigit():
#         if int(user_input) > 100:
#             print(f"You chose the number {user_input}.")
#             for x in range(2, int(user_input) - 1):
#
#                 if int(user_input) % x == 0:
#                     print("Not Prime")
#                     continue
#                 else:
#                     print("Prime!")
#                     break
#         else:
#             print("Please try again.\n")
#     else:
#         print("Please ensure you are entering a number.")





    # for x in range(2, int(user_input)-1):
    #
    #     if int(user_input) % int(x) == 0:
    #         print("Not Prime")
    #     else:
    #         print("Prime!")

    # if int(user_input) % int(user_input) == 1:
    #     print("Success")
    # else:
    #     print("Fail")

# create boolean to test for prime/not prime.

prompt = True
while prompt:

    user_input = input("Enter a number greater than 100.\n")
    NOTprime = True

    if user_input.isdigit():
        if int(user_input) > 100:
            print(f"You chose the number {user_input}.")
            for x in range(2, int(user_input) - 1):

                if int(user_input) % x == 0:
                    NOTprime
                    print("NOT Prime!")
                    break
                else:
                    print("Prime!")
                    break
        else:
            print("Please try again.\n")
    else:
        print("Please ensure you are entering a number.")

