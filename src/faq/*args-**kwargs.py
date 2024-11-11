'''
不定参数
'''

def func_args(*args):
    for arg in args:
        print(arg)

def func_kwargs(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    func_args(1, 2, 3, 4)
    func_kwargs(a=1, b=2, c=3)
