'''
try-except-else-finally
'''

def divide(x: float, y: float) -> float:
    try:
        res = x / y
    except ZeroDivisionError:
        print('division by zero!')
    except TypeError:
        print('should be number!')
    else:
        print(f'result is {res}')
    finally:
        print('exe finally.')


if __name__ == '__main__':
    divide(2, 0)    # ZeroDivisionError
    divide(2, 1)    # 2.0
    divide('2', 1)  # TypeError