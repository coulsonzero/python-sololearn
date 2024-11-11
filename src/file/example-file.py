def read_file():
    with open("test.txt", encoding="utf8") as fp:
        for line in fp:
            print(line)
    '''
    hello this is a text

    you could change it
    
    in here
    '''

    with open("test.txt", encoding="utf8") as fp:
        print(fp.read(5))
    # "hello"

    with open("test.txt", encoding="utf8") as fp:
        print(fp.read())
    '''
    hello this is a text
    you could change it
    in here
    '''

    with open("test.txt", encoding="utf8") as fp:
        print(fp.readline())

    # hello this is a text

    with open("test.txt", mode="r", encoding="utf8") as fp:
        print(fp.readlines())
    # ['hello this is a text\n', 'you could change it\n', 'in here']

if __name__ == '__main__':
    read_file()