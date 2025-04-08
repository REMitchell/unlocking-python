from cdraw2.shapes.base import Shape

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def draw(self, printer=print):
        self.do_loading()
        for _ in range(0, self.height):
            printer('#' * self.width)
