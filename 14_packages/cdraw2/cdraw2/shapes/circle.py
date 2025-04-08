import math
from cdraw2.shapes.base import Shape

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self, printer=print):
        self.do_loading()
        for i in range(-self.radius, self.radius + 1):
            y = math.sqrt((self.radius**2) - (i**2))
            y = round(y)
            printer(' ' * (self.radius - y) + '#' * (y * 2))
