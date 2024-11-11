class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def square(cls, side_len):
        return cls(side_len, side_len)

    @staticmethod
    def valid():
        return "hello Rectangle."


if __name__ == '__main__':
    squ = Rectangle.square(5)
    print(squ.area())   # 25
    print(squ.valid())  # hello Rectangle.