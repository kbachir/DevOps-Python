# FUNCTIONS!

# def woof():  # def xxx():  is how you define a function.
#     print("WOOF!")  # the logic that belongs to this function needs to be indented.
#
# woof()
# woof()
# woof()  # you can then call this function very simply whenever you want.


# def woof(number_of_woofs):  # essentially, you're requesting that user fills in the brackets to complete a variable.
#     for i in range(number_of_woofs):
#         print("Woof!")
# # you can multiply strings by int:
#     print("Woof!" * number_of_woofs)
#
# woof(17)



# def greeting(name):
#     print(f"Hello to you, {name}")
#
# greeting("Karim")



def double_plus_num(num1, num2=1):  # (by adding an equals to one of the arguments, we are setting a default value.
    # note: Default arguments can only come after the first arg, as that has no default. How will Py know which arg (i.1 num1, num2, num3 etc) user is entering?

    # double the first number and then add the second
    ans = (num1 * 2) + num2  # ans is only defined within the function here. If we want to use it outside of this function, we need return.
#    print(ans)
    return ans


#  double_plus_num(2, 6)  # 2 * 2 + 6 = 10

# x = double_plus_num(5, 2)
# print(x, x, x)  # x is being returned outside of the function.

#  What about if you don't know how many arguments you want to specify in a function? I.e print() can have endless args, 1, 2, 3, 4, 5, etc
#  Multi args:
#
# def shopping(*items):
#     print(items, type(items))  # do not include the asterisk when referencing the argument in other code. It will then register "items" in this case as a tuple:
#
# shopping("banana", "apple", "orange")


# def shopping(*items):
#     for item in items:
#         print(f"Don't forget to buy an {item}")
#         print(f"Don't forget to buy {items}")
#
# shopping("banana", "apple", "orange")
#

# def shopping(name, *items):
#     for item in items:
#         print(f"{name}! Don't forget to buy an {item}")
#
# shopping("Karim", "banana", "apple", "orange")  # the first item becomes the first argument.


# def shopping(name, *items, shout=False):
#
#     if shout:
#         name = name.upper()
#
#     for item in items:
#         print(f"{name}! Don't forget to buy an {item}")
#
# shopping("Karim", "apple", True)  # this doesn't work.
# shopping("Karim", "apple", shout=True)  # this works because you are specifying which optional argument you are calling upon.



def greeting(name):
    print(f"Hello to you, {name}")  # it is expecting a string here, though it doesn't have to be. This only works because we're using an f string right now.
    # if you didnt use an f string i.e print("hello, " + name), it will break.
    # Py allows you to specify a type hint for arguments. This looks like 'def greeting(name: str):'. Note this is not an enforcable rule, just a hint/guide.
    # If you add default parameters to type hint args, it starts to look messy such as 'def greeting(name: str = David)' <--- this is assigning a default value of David to a type hint of str for arg name.


def double_plus_num(num1: int, num2: int): -> int:  # type hint for output, Pycharm actually understands this and knows what output to expect. Again, only a hint.
    ans = (num1 * 2) + num2
    return ans


#  Good Practices:
#  Functions should have clear names that say what they do. Even if its longer and wordier. Make sure arguments are clearly worded too.
#  always lowercase
#  any function that doesn't return anything automatically returns None
#  keep your my_functions small. If they're too big, redesign so that your function incorporates smaller my_functions.
#  [ """   text   """ and pass ] is a way for you to detail instructions at the start of a function. This is known as a doc string. You can do it before of above. Preferably inside.

pass  # pass does nothing. It just continues on... it's a way to leave a function temporarily empty too.
continue  # continue tells it to continue a loop. So continue onto the next iteration. In while loops, it will just restart. In for loops, it will go to the next interation of the for loop.