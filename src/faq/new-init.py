class Myclass:
    def __init__(self, value):
        self.value = value
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

if __name__ == '__main__':
    a = Myclass(10)
    print(a.value)  # 10
