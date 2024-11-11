'''
is: 比较引用是否相同，
==：比较值是否相同
'''

def example_is():
    # 对于不可变数据类型（整数、字符串、元组)
    a = 1
    b = 1
    print(a is b)   # True

    # 可变数据类型（列表、字典、类实例）
    c = [1, 2, 3]
    d = [1, 2, 3]
    print(c is d)   # False

def example_eq():
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b)   # True


if __name__ == '__main__':
    # example_is()
    # example_eq()
    example_none()