import math 

PI = 3.14159

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        for i in range(-self.radius, self.radius + 1):
            y = math.sqrt((self.radius ** 2) - (i ** 2))
            y = round(y)
            print(' ' * (self.radius - y) + '#' * (y*2))


def square(n=5):
    for _ in range(n):
        print('#'*n)

print(f'Module name is: {__name__}')

if __name__ == '__main__':
    print('This should be imported, not run directly!')