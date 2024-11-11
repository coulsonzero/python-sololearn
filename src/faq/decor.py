def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def decor2(func):
    def wrap():
        print("-------------")
        func()
        print("-------------")
    return wrap

@decor2
@decor
def print_text():
    print("Hello world!")


print_text()
'''
-------------
============
Hello world!
============
-------------
'''