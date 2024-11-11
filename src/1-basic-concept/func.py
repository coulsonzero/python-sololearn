def lib():
    return "hi"

class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print(f"Hi from {self.name}")