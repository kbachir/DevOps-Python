from math import floor


class Rectangle:

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def __str__(self):
        return f"({self.length, self.width})"

    def __repr__(self):
        return f"({self.length, self.width})"

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length * 2) + (self.width * 2)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
#        self.area = self.get_area()

    def __str__(self):
        return f"({self.length})"

    def __repr__(self):
        return f"({self.length})"

    # def get_number_enclosing(self, small_square):
        #  return floor(self.length / small_square)


    def get_number_enclosing(self, small_square):
        # return (int((self.get_area() / small_square.get_area()) ** 0.5)) ** 2
        # self.get_area / small_square.get_area() ** 0.5 * 2

