from cdraw2.shapes.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.height = size
        self.width = size
