#Input is useful, but our end goal is automation, so we ideally wouldn't be using it much. We don't want to have to slow down and wait for human input.

# name = input("What is your name?\n")
# # \n = "new line"
#
# print("Hello, " + name".")

# firstName = input("What is your first name?\n")
# surName = input("What is your surname?\n")
# age = int(input("What is your age in years?\n"))
#
# print("Hello " + firstName + surName + ", you are " + str(age) + " years old.")
#
# print(f"") # formatted string
# print(f"You are {age} years old.")

# year_of_birth = int(input("Please enter your year of birth\n"))
# age = 2022 - year_of_birth
#
# print("Hello " + firstName + surName + ", you are " + str(age) + " years old.")

# birth_month = int(input("Please enter your birth month as a number\n"))
# birth_year = int(input("Please enter your year of birth\n"))
# age = ((12, 2022) - (birth_month, birth_year))
#
# print(firstName + " " + surName + " is " + str(age) + " years old.")

#=========================================================================

firstName = input("What is your first name?\n")
surName = input("What is your surname?\n")
age = int(input("What is your age in years?\n"))

print(f"Hello " + firstName + " " + surName + ", " + f"you are {age} years old.")


