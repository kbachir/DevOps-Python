# OOP - Object Oriented Programming
#  For classes, naming convention is no underscore and capital initials. I.e VeryGoodDog.
# class Dog:
#
#     animal_kind = "canine"  # class variable
#             #self means referring to the current class. The first argument has to be the class itself. You don't need to enter
#             #any argument in bark because fido, being a dog, has fulfilled that class argument requirement. You can still add arguments, and if you do, you need to provide that first argument,.
#     def bark(self):  # this is called a method. They look like my_functions here.
#         return "Woof!"



# fido = Dog()
# print(fido, type(fido))  # <- where it lives, what class its from, memory
# print(fido.animal_kind)
# print(fido.bark())

# fido = Dog()  # <- Instantiation - i.e creating an INSTANCE of a class.
# lassie = Dog()
# axel = Dog()
#
# fido.animal_kind = feline  # objects can adapt and change, even if they're from the same template. This will also overwrite all future instances of dog.animal_kind.
#  if you change the class variable, it will affect future instances of that class.

#  we don't want this to happen easily to our objects. I.e cookie cutter, if you cut a cookie using it, change the shape
#  and cut another, the already cut cookie shape shouldn't change.
#  You do this by setting attributes:
#  This uses a special method that is called whenever an object is instantiated. Whenever an instance is made,
#  an object goes thru initialisation. This is __init__(self):

class Dog:             # v you can add more parameters that need to passed in. I.e dog breed.
    def __init__(self, dog_breed):  # initialisation, dunder (double underscore) init
        #  animal_kind = canine #  this is where you set the attribute. However, this limits the scope.
        self.animal_kind = "canine"                    # the way you fix this is with self.

        #  any attributes you want a class to have go within the dunder init method. This still allows you to change
        #  the attributes of an instance later, but it won't change the default for other instances.
        self.breed = dog_breed
        #  dog_breed will be passed in as an argument/parameter. The thing we pass in, we use as a variable
        #  and assign it to be an attribute. Convention is to use the same word for both. I.e. self.breed means that
        #  the parameter should also be called breed, not dog_breed. We used dog_breed just for examples sake.
        #  self.breed is an attribute, breed is a variable.


class cat:
    def __init__(self, breed, colour):
        self.animal_kind = "Feline"
        self.breed = breed
        self.colour = colour
        #self.hairtype = [short, long]

    def soft_purr(self):
        return "prrrrrr I'm a pointless animal"

milo = cat("tabby", "grey")


print(milo)
print(milo.animal_kind)
print(milo.breed)
print(milo.colour)
