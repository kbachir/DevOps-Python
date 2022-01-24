age = 17
film_showing = True

# if age >= 18:
#     print("You are allowed to buy a ticket for this film.")
#     print("Enjoy the film!")
#^4space indentation. See bottom right corner of pycharm. "4 spaces"

# if age >= 1:  # (Boolean value = True)
#     print("You are allowed to buy a ticket for this film.")
#     print("Enjoy the film!")

# if age >= 18 and film_showing:
#     print("You are allowed to buy a ticket for this film.")
#     print("Enjoy the film!")
# elif age < 18:
#     print("You are not old enough.")
# elif age == 17:
#     print("Come back next year.")
# elif not film_showing:
#     print("This film is not showing.")
# else:
#     print("No dice")
#
# print("This will always print.")

certificate = '18' # U, PG, 12, 12A, 15, 18
# Check the certificate
# Print corresponding info about the film

if certificate.upper() == 'U':
    print('Suitable for all ages.')
elif certificate.upper() == 'PG':
    print('Requires parental consent.')
elif certificate <= '12' or certificate == '12A':  # if you just wrote if ceritficate == 12 or 12A, it will always resolve true as a string will always resolve true re boolean.
    print('Suitable for all children aged 12 and above.')
elif certificate <= '15':
    print('Suitable for all children aged 15 and above.')
elif certificate <= '18':
    print("Adults only.")
else:
    print("Certificate not recognised.")


