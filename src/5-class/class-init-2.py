class Student:
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print(f"Hi from {self.name}")


if __name__ == '__main__':
    s = Student("Bob")
    print(s.name)
    s.sayHi()