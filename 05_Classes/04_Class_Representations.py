class Location:

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):  # a good repr will return something that looks a lot like source code.
        return f"Location(latitude={self.latitude}, longitude={self.longitude}"

    def __str__(self):  #  supposed to return more human friendly information.
        return f"({self.latitude}, {self.longitude}"

    
bham_academy = Location(52.123, -52.123)
print(bham_academy)  # this is not clean, we'd much prefer a clean representation. This is where __repr__ comes in.