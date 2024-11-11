class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")


# class inheritance
class Cat(Animal):
    def purr(self):
        print("purr...")


class Dog(Animal):
    # method override
    def bark(self):
        print("Woof!")

    def bof(self):
        # method inheritance
        super().bark()


if __name__ == '__main__':
    fido = Dog("Fibo", "brown")
    print(fido.color)
    fido.bark()
    fido.bof()