class Car:

    def __init__(self, max_speed=100):
        self.current_speed = 50
        self.max_speed = max_speed


    def acceleration(self, speed_increase=0):

        new_speed = self.current_speed + speed_increase
        if new_speed < self.max_speed:
            return new_speed
        else:
            return self.max_speed

    def decelerate(self, speed_decrease=0):

        new_speed = self.current_speed - speed_decrease
        if new_speed >= 1:
            return new_speed
        else:
            return "You have stopped."
