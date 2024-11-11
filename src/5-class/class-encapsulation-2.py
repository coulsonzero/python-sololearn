class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)


if __name__ == '__main__':
    s = Spam()
    s.print_egg()

    # error
    # print(s._Spam__egg)
    # print(s.__egg)