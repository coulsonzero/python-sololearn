def init():
    s = 'hello world'
    s = "hello world"
    s: str = "hello world"

    # '\'
    s = 'I\'m John Smith'
    s = "I'm John Smith"

    s = """this
    is a multiline 
    text"""

    s = "A\nB\nC"

def demo():
    s: str = "Hello World"
    print(s.find("lo"))   #
    print(s.index("lo"))  #

if __name__ == '__main__':
    demo()


