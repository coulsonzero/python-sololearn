class Number:
    def __init__(self, num):
        self.value = num

    @property
    def isEven(self):
        return self.value % 2 == 0


if __name__ == '__main__':
    num = int(input())
    x = Number(num)
    print(x.isEven)
