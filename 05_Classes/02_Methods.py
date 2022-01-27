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

GTR = Car()

print(GTR)
print(GTR.max_speed)
print(GTR.current_speed)
print(GTR.decelerate(10))
print(GTR.acceleration(10))
print(GTR.acceleration(100))
print(GTR.decelerate(100))


# def check_attributes(vehicle):
#
#     for i in vehicle:
#         print(i)
#         print(i.max_speed)
#         print(i.current_speed)
#         print(i.decelerate(10))
#         print(i.acceleration(10))
#         print(i.acceleration(100))
#         print(i.decelerate(100))
#
# check_attributes(GTR)