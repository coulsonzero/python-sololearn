class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")


if __name__ == '__main__':
    felix = Cat("ginger", 4)
    rover = Cat("dog-colored", 4)
    stmpy = Cat("brown", 3)

    print(felix.name)