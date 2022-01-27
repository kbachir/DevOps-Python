# # import random
#
# from random import random, randint  # you want to import the specific library as the whole library means you'll have to
# #do random.random every time for example. See randint example.
# from math import ceil, floor, pi
# #  import math as m // you can give a package an alias so its easier to work with. Careful not to override other stuff.
# import os  # stuff to do with system info.
#
#
#
# print(random())
# print(random())
# print(random())
# print(random())
#
# print(pi)
# print(ceil(pi))
# print(floor(pi))
#
# print(randint(1, 100))

# import Packages06.my_functions.my_test_functions as f
#
# print(f.work_dir)

#  PIP -> PIP Installs Packages (Auto-acronym)

import requests  # hover over requests and click link for PyCharm to take care of PIP installations.
#  to uninstall; pip uninstall requests
#  or click on the "Python Packages" tab at the bottom of the screen. Then you can search "Requests"

r = requests.get("https://www.bbc.co.uk")
#  print(r, type(r))  # showing us status code
#  print(r.content)  # shows the html of BBC homepage.
#  print(r.status_code)


# arf = requests.get("https://www.alridha.org")
# print(arf)
# print(arf.content)