s = """hello, world
welcome to here!
"""


def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


@uppercase_decorator
def display_text(text):
    return text


print(display_text(s))
'''
HELLO, WORLD
WELCOME TO HERE!
'''