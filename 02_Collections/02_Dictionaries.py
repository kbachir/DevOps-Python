# Dictionaries!

# Key-Value Pairs

# my_dict = {'key': 'value'}  # the key is usually a string, the value can be absolutely anything. int, str, tuple, another dict anything.

# table = {
#     'name': 'The Table',
#     'colour': 'light brown',
#     'height': 120,
#     'length': 200,
#     'width': 150
# }
#
# print(table)
# print(table['colour'])  # DICTIONARY NAME [ NAME OF KEY ]
#
# table['price'] = 99.99  # you can add keys like this too
# print(table)
#
# table.update({'price': 99.99, 'height': 125})  # .update method to update the dictionary.
# print(table)
#
# print(table.get('price'))  # .get can retrieve info from a dictionary
#
# print(table.get('price'))
# print(table('price'))
# square brackets will return an error if a key isnt present, the .get method will either return None or allow you to specify a default value. i.e
# print(table.get('legs', 'Key Missing'))  # vs
# print(table['legs'])


table = {
     'name': 'The Table',
     'colour': 'light brown',
         'dimensions': {
         'height': 120,
         'length': 200,
         'width': 150
         }
}  # You can make dictionaries within dictionaries, as above

print(table['dimensions']['width'])
print(table.get('dimensions').get('width'))  # you would use the .get method in order to ensure a failsafe. If the key doesn't exist, the whole programme will crash, and you can save that by using .get

# print(table['colour'], (dimensions['height']))

# how do you use them all in conjunction? What order should you store things in or do you keep them independent?

# METHODS FOR DICTIONARIES:
print(table.keys())
print(table.values())
print(table.items())

