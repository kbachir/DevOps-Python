print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def divisor(n1: int):

    divisor_list = []

    for n in range(1, n1+1):
        if n1 % n == 0:
            divisor_list.append(n)
    print(divisor_list)

divisor(12)

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def factor_check(n1: int, n2: int):

    if n1 % n2 == 0:
        print(True)
    else:
        print(False)

factor_check(10, 6)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

#A2a:

def letter_index(letter):

    #for i in alphabet:
    print(alphabet.index(letter))

letter_index(' ')


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

input = input("enter name")

def name_index(name):

    new_list = []

    for i in name:


        new_list.append(alphabet.index(i))
        return new_list

name_index(input)

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password(passw):

    password_list = []

    for i in passw:

        password_list.append(sum(i))

    print(passw)

password(new_list)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:



print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #