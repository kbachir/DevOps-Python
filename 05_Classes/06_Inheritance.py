# Inheritance and Polymorphism (polymorphism = things can take many forms)

class Mammal:
    def __init__(self, name):
        self.warm_blooded = True
        self.name = name

    def reproduce(self):
        print("Giving birth to live young")

class Platypus(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.poisonous_barbs = True
        # self.warm_blooded = False

    def reproduce(self):
        print("Lays eggs.")



class Horse(Mammal):  # Inheriting from Mammal class

    def __init__(self, name, jockey):  # This init overrides the new one as you can only have one method of the same name.
        # we need to tell this class to also run the init method of parent class.
        super().__init__(name) #  to pass arguments thru super init, you need to create the arg in both super class init and new init
        # super refers to the parent class - meaning when we init horse, we also run the init for
        # the Mammal class.
        self.legs = 4
        self.jockey = jockey

    def pregnancy(self):
        print("Wait 11 months...")
        super().reproduce()  # use super for calling parent class methods too.

class Pony(Horse):
    def __init__(self, pony_name, cuteness_rating=10):
        super().__init__(pony_name, None)

    def give_birth(self):
        super().reproduce()


# i.e.
#p = Pony
# h.reproduce()
#p.reproduce()

perry = Platypus("Perry")
perry.reproduce()