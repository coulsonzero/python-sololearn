def test_pass():
    print("start")
    pass
    print("end")


def test_return():
    print("begin")
    return
    print("end")


if __name__ == '__main__':
    test_pass()
    # test_return()

# start
# end