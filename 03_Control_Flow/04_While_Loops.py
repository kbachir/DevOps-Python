# For Loops iterate over a set length. It has a limited amount of times that it will run.
# While Loops can run indefinitely until a certain condition is met.

# i = 1
#
# while i <10:
#     print(i)
# #    i = i + 1
#     if i == 5:
#         print("FIVE PARTY!")
#         break  # break will break you out of the nearest loop
#     i += 1
#
# print("Finito")


# keep_looping = True
#
# while keep_looping:
#     print(i)
#     if i == 5:
#         print("FIVE PARTY!")
#         keep_looping = False   #  Changing the condition doesn't instantly break you out of a loop. It finishes the loop first (it still prints "start again")
#     i += 1
#     print("start again")
#
# print("Finito")


# for x in ['a', 'b', 'c', 'd', 'e']:
#
#     break_for = False
#
#     i = 100
#     while i < 110:
#         print(x, i)
#         if i == 105:
#             break_for = True
#             break
#         i += 1

#print("Close")


# age = input("What is your age?\n")
#
# if age.isdigit():   # isdigit is different to isnumeric as some characters are numeric but not digits, i.e a single character that encompasses 1/2
#     int_age = int(age)
# else:
#     print("Please enter age in digits!")
#     age = input("What is your age?\n")

# age = None
# prompt_user = True
#
# while prompt_user:
#
#     age = input("What is your age?\n")
#
#     if age.isdigit() and age <= 119:  # remember with the and, it checks the first requirement and then the second
#         prompt_user = False
#     else:
#         print("Please enter age in digits!")
#
# print(f"Double your age is {int(age) * 2}")


# age = None
# prompt_user = True
#
# while prompt_user:
#
#     age = input("What is your age?\n")
#
#     if age.isdigit():
#         if int(age) <= 119:
#             prompt_user = False
#         else:
#             print("You are not that old.")
#     else:
#         print("Please enter age in digits!")
#
# print(f"Double your age is {int(age) * 2}")



r_low = None
prompt = True

while prompt:

    r_low = input("Pick a number")

    if r_low.isnumeric():
        if int(r_low) > 0:  # if you don't specify int() for the variable, Py still tries to concatenate str and int.
            prompt = False
        else:
            print("Must be larger than zero.")
    else:
        print("Please enter a digit")

print("Well done, you have entered a digit.")

#  DRY RULE: Don't repeat yourself. This is where my_functions come into play.

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:  = if we wanted to change from factor of 5, this would be difficult. This is considered hard coding. Instead, we can do as follows:
#         print("FIZZBUZZ!")
#     elif number % 3 == 0:
#         print("Fizz!")
#     elif number % 5 == 0:
#         print("Buzz!")
#     else:
#         print(number)


# fizz = 3  # This code is much more friendly and malleable. We can swap things out very easily.
# buzz = 5

# for number in range(1, 101):
#     if number % fizz == 0 and number % buzz == 0:
#         print("FIZZBUZZ!")
#     elif number % fizz == 0:
#         print("Fizz!")
#     elif number % buzz == 0:
#         print("Buzz!")
#     else:
#         print(number)