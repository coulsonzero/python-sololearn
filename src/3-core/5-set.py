def set_example():
    se = {3, 1, 6, 2}
    se.add(7)       # {1, 2, 3, 6, 7}
    se.pop()        # {2, 3, 6, 7}}
    se.remove(2)    # {3, 6, 7}
    # se.clear()    # {}
    print(se)

if __name__ == '__main__':
    set_example()
