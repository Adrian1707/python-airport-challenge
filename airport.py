import random

class Airport:

    def __init__(self, capacity = 5):
        self.planes = []
        self.capacity = capacity

    def land(self, plane):
        if len(self.planes) >= self.capacity:
            raise CapacityReachedError("No more space left in airport")
        if self.weather_is_stormy():
            raise StormyWeather("Not suitable for flying")

        self.planes.append(plane)

    def take_off(self, plane):
        self.planes.remove(plane)

    def weather_is_stormy(self):
        if random.randint(1,100) <= 30:
            return True
        else:
            return False

class CapacityReachedError(Exception):
    pass

class StormyWeather(Exception):
    pass

