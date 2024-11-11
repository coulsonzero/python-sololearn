def example():
    se = set({3, 1, 6, 2})
    print(se)  # {1, 2, 3, 6}

    se.pop()   # {2, 3, 6}
    print(se)

def add():
    se = {3, 1, 6, 2}
    se.add(7)       # {1, 2, 3, 6, 7}
    se.pop()        # {2, 3, 6, 7}}
    se.remove(2)    # {3, 6, 7}
    # se.clear()      # {}
    print(se)

if __name__ == '__main__':
    # example()
    add()