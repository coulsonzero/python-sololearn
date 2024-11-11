# coding: utf-8
from functools import wraps


class Test(object):
    def __init__(self):
        self.reset = True
        self.flag = True

    # 在类里定义一个装饰器
    def info(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print('log_type: info'.center(50, '-'))
            if self.reset:
                print('Reset is Ture, change flag...')
                self.flag = False
            return func(self, *args, **kwargs)
        return wrapper

    @info
    def speak(self, text):
        print(f'speak: {text}')


if __name__ == '__main__':
    t = Test()
    t.speak('hello world')
    print(t.flag)