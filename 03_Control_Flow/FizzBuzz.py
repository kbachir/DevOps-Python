# For numbers 1 to 100
# Play fizzbuzz
# Print number
# If divisible by 3, fizz
# If divisible by 5, buzz
# if both, fizzbuzz

# What can you add?
# Can we customize the end number?
# Or the start number?
# Can we get those from player input?
# Can we input alternate words for fizz and buzz



# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FIZZBUZZ!")
#     elif number % 3 == 0:
#         print("Fizz!")
#     elif number % 5 == 0:
#         print("Buzz!")
#     else:
#         print(number)


while True:

    while True:

        custom_words = str(input("Would you like to input custom words?\n"))

        if custom_words.upper() == "YES":
            fizz = str(input("Pick a word to replace 'Fizz'.\n"))
            buzz = str(input("Pick a word to replace 'Buzz'.\n"))
            break
        elif custom_words.upper() == "NO":
            fizz = "fizz"
            buzz = "buzz"
            break
        else:
            print("Simple answers: Yes or No?")

    while True:

        try:
            r_low = int(input("Pick a minimum number!\n"))
        except:
            print("That's not a number dude... try again")
        else:
            if r_low > 0:
                break
            else:
                print("It needs to be larger than 0 bud.. c'mon")


    while True:

        try:
            r_high = int(input("Pick a maximum number!\n"))
        except:
            print("That's not a number dude... try again")
        else:
            if r_high > r_low:
                break
            else:
                print("It has to be higher than you're minimum input too.")


    for number in range(r_low, r_high+1):

        if number % 3 == 0 and number % 5 == 0:
            print(fizz + buzz)
        elif number % 3 == 0:
            print(fizz)
        elif number % 5 == 0:
            print(buzz)
        else:
            print(number)

    while True:

        play_again = str(input("Would you like to play again?\n"))

        if play_again.upper() == "YES":
            break
        elif play_again.upper() == "NO":
            print("Thanks for playing!")
            exit()
        else:
            print("Simple answers bud, Yes or No?")

