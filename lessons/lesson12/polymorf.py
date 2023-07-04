print(5)

print("hell")

print([1, 2, 3])


def convert_to_string(arg):
    return str(arg)


print(convert_to_string(5))
print(convert_to_string("hello"))
print(convert_to_string([1, 2, 4]))


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        print(f"Render shape with the pint: x: {self.x}, y: {self.y}")


class Sercle(Shape):
    def __init__(self, x, y, radius):
        Shape.__init__(self, x, y)
        self.radius = radius

    def render(self):
        print(f"Render circle with the center in the point x: {self.x}, y: {self.y} and radius {self.radius}")


shape = Shape(5, 4)

circle = Sercle(5, 4, 10)

shape.render()
circle.render()
