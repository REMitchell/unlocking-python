from draw.base import Shape

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def draw(self):
        for i in range(0, self.height):
            print('#' * self.width)
