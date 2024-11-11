import re

class ReExample:
    def example_re(self):
        s = "$1800, 卫衣, 90"
        p = re.compile('\d+')
        res = p.findall(s)
        print(res)
        # ['1800', '90']

    def example_re2(self):
        result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
        print(result)
        # [('width', '20'), ('height', '10')]

if __name__ == '__main__':
    r = ReExample()
    r.example_re()