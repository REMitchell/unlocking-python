from cdraw.colors.colors import DEFAULT

class ColorPrinter:
    def __init__(self, text_color='', background_color=''):
        self.text_color = text_color
        self.background_color = background_color

    def print(self, string):
        print(f'{self.text_color}{self.background_color}{string}{DEFAULT}')
