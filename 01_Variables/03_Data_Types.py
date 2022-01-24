# Numeric!

# i = 375  # int
# f = 3.75  # float
# c = 3j + 2  # complex number
#
# print(c, type(c))
#
# add = 3 + 5
# subtract = 3 - 5
# multiply = 3 * 5
# divide = 3 / 5 # // will return an int (whole number) instead of a float
# power = 3 ** 5  # to the power of
# modulo = 3 % 5  # remainder after division. Use cases for working out actions for repeating sequences.
# # square root/cube root = x ** 0.5 or 1/2 / 1/3

# Strings!
#
# single = 'You can use single quotes'
# double = "You can use double quotes!"
# # mix = 'You can't use both"
# fix = 'You can tell python\'s brain to ignore the special function of a character using an escape character: \ .'
# print(fix)
#
#
# # Indexing and Slicing!
#
# hi = "Hello World!"
# print(hi[6])  # Indexing a character in a string and printing just that index (remember, Py starts counting at 0).
# print(hi[-1])  # Using a negative number will start counting from the end backwards.
# #print "lo wo"
# print(hi[3:8])  # Displays a range of indexed characters. NOT INCLUSIVE OF LAST INDEX. I.e 6:11 will not include 11.
#
# print(len(hi)) # len() will return the length of the string

# Methods!

# white_space = "      ..lots of white space..       "
# # print(len(white_space)) # will return 32. But most of that is just empty spaces. You can do the following:
# # print(white_space.strip())  # strip = strip of spaces, lstrip() and rstrip() strip from left but not right or right but not left.
# # # vs
# # print(white_space)
# print(white_space.count(" "))
# print(white_space.replace("o", "ooooo"))
# print(white_space.strip().capitalize())  # you can chain type methods together (i.e multiple string methods)


# F-Strings! (formatted strings)

# pi = 3.14159265359
# print(pi)
# print(f"pi to 3dp: {pi:.3f}")  # 'Pi to 3 decimal places: f"pi: to 3 decimal places'
#
# score = 16
# max_score = 26
#
# print(f"You scored {score / max_score}")
# print(f"You scored {score / max_score:.2%}")  # can also format to percentage, and then format to a particular decimal too.
#

#  Boolean!

t = True
f = False

# print(t, type(t))
#
# print(5 == 5)  # returns true.
# print(12 % 3 == 0)
# print(3 != 5)
#
# # Very useful for a lot of operators ( == != * !* etc )

# age = 19
# drink = "alcohol"
#
# print (age > 18 and drink == "alcohol")

hi = "Hello World"
print(hi.isalpha())
print(hi.islower())
print(hi.isupper())
print(hi.endswith("d"))
print(hi.startswith("F"))

hi = "Hello World."
print(hi.isalpha())
print(hi.islower())
print(hi.isupper())
print(hi.endswith("d"))
print(hi.startswith("h"))


name = input("Type your name")
age = int(input("enter age"))

print(f"{name} {age}")