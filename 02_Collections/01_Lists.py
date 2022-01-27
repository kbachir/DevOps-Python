# Lists!

# shopping_list = ["eggs", "bananas", "tea", "bread"]
# print(shopping_list, type(shopping_list))
#
# print(len(shopping_list))
# print(shopping_list[0:2])  # displays index of item in list
#
# shopping_list[2] = "milk"  # can replace items within list based on index position.
# print(shopping_list)
#
# shopping_list.append("biscuits")  # Append adds an item to the end of a list. Its an example of a method that changes the variable we call it upon, instead of just returning something like other methods. Append only wants you to add one object at a time
# print(shopping_list)


# shopping_list.append("bread")
# shopping_list.append("bread")
#
# #shopping_list.remove("bread")  # if you have multiple instances of the same item, it will remove the first instance of that item. I.e if there are three breads in your list, it will remove the first occurence of bread.
# print(shopping_list)
#
# shopping_list.pop(-1)  # remove is based on values. Pop is based on the index/position within the list. Unlike .append, .pop is a method that both changes the list and returns the item it popped out.
# print(shopping_list)

# mixed = [1, 2, "three", True, False, ["Four", "Five"]]
#
# mixed[1] = 2.0  # Lists are mutable, meaning they can be changed (mutated)
# print(mixed)
# print(mixed[2:5:2])  # will print 2 thru 4 but skip in 2s
# print(mixed[::3])  # will go through everything and pull out every 3rd thing
#
# print(mixed[5][0])  # 'mixed[5]' is a list, so if you add an index position after that, itll pull that item. If you do that again, it'll pull from the string:
# print(mixed[5][0][1])
#
# sublist = mixed[5]
# print(sublist)
#
# mixed[5] = ["a", "b"]
# print(sublist)  # doesnt work
#
# sublist[0] = "a"
# print(sublist)  # does work
#
# # lists are weirdly complicated: look at this
# mixed[5][1] = "b"
# print(mixed)
# print(sublist)

# Tuples!

# colours = ("red", "blue", "green")
# print(colours, type(colours))
#
# print(colours[0])
# colours[0] = "maroon"

# Tuples are IMMUTABLE. That's why there are barely any tuple methods too.
# .count = how many times does an item appear in a tuple.
# .index = finds out where something lives in the tuple.

list_in_tuple = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

print(len(list_in_tuple))
list_in_tuple[0][-1] = "Success"
print(list_in_tuple)

list_in_tuple[0].append("sucess")
print(list_in_tuple)

# changing an item within a list that lives in a tuple is possible, but you can't change the list itself (?)

"""

# Split

text = "It was the best of times"

text_list = text.split() <- string operators that splits a string into word by word list.

csv = "12, 235, 645, 564, 234"

csv_list = csv.split(",") <- split csv numbers into file by commas. 

# Join

text_list = " ".join(text_list) <- prints a list for view as a string. Will return a string but not change the original. 

# Sorted

sorted(n) <- Will sort whatever you give it. It will return but not change original again. 
n.sort <- Will actually change the list and sort it. 

"""