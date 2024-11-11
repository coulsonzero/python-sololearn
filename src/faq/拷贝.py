import copy

def example_copy():
    a = [[1, 2, 3], [4, 5, 6]]
    # b = a[:]
    b = copy.copy(a)
    b[0][0] = 0
    print(a)
    print(b)


# notice!
def example_copy2():
    a = [1, 2, 3, 4]
    b = copy.copy(a)
    b[0] = 0
    print(a, b)


def example_deepcopy():
    a = [1, 2, 3, 4]
    # b = a[:]
    b = copy.deepcopy(a)
    a[0] = 0
    print(a)    # [0, 2, 3, 4]
    print(b)    # [1, 2, 3, 4]

if __name__ == '__main__':
    example_copy()
    # example_deepcopy()