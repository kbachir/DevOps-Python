pokemon = {'Bulbasaur', 'Squirtle', 'Charmander'}
# sets are built in the same way as dictionaries re syntax, but there are no keys or pairs etc.
print(pokemon, type(pokemon))

# methods

pokemon.add('pikachu')
print(pokemon)

# Sets are UNORDERED and MUTABLE. They are not subscriptable, meaning we cannot use square brackets at the end to ask for an index or slice. There is no set order to them.

pokemon.discard('Bulbasaur')  # case-sensitive
print(pokemon)

pokemon.add('Pikachu')
pokemon.add('Pikachu')
print(pokemon)  # You cannot have duplicates. Only one of each thing, each item has to be unique.

l = [1, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 5, 8, 9,]
print(l)
print(set(l))  #set() will remove duplicate values

# Frozen Sets

x = frozenset(['let', 'it', 'go'])
print(x)

# Frozen sets are immutable sets. Everything else is the same. .add and .remove are not available