import math
from draw.base import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        for i in range(-self.radius, self.radius + 1):
            y = math.sqrt((self.radius**2) - (i**2))
            y = round(y)
            print(' ' * (self.radius - y) + '#' * (y * 2))
