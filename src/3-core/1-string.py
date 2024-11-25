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

def example_string():
    s: str = "Hello World!"
    print(s.find("lo"))   # 3
    print(s.index("lo"))  # 3
    print(s.count("o"))   # 2
    print(s[0])           # 'h'
    print(s.split())      # ['Hello', 'World!']
    print(s.split(','))   # ['Hello World!']
    print(''.join(['hello, world!']))   # 'hello, world!'
    print(s.replace('!', '?'))          # 'Hello World?'
    print(s[::-1])        # !dlroW olleH

if __name__ == '__main__':
    example_string()


