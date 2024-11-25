class Car(object):
    salePrice = 150000
    __discountPrice = 120000
    def __init__(self, name1, name2):
        self.name1 = name1
        self.__name2 = name2

if __name__ == '__main__':
    print(Car.salePrice)
    print(Car._Car__discountPrice)
    c = Car('大众', '高尔夫')
    print(c.name1)
    print(c._Car__name2)
