import math


class Rectangle:
    def __init__(self, required_width, required_height):
        self.width = required_width
        self.height = required_height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, required_width):
        self.width = required_width

    def set_height(self, required_height):
        self.height = required_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        symbol = "*"
        pics = ""
        if 50 < self.width or 50 < self.height:
            return "Too big for picture."
        else:
            for i in range(0, self.height):
                pics += f"{self.width * symbol}\n"
        return pics

    def get_amount_inside(self, shape):
        return math.floor(self.get_area() / shape.get_area())


class Square(Rectangle):
    def __init__(self, required_side):
        self.side = required_side
        super().__init__(required_side, required_side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, required_side):
        self.width = required_side
        self.height = required_side
