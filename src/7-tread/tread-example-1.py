import threading
import time


def func(x, y):
    for i in range(x, y):
        print(i, end='')
    time.sleep(10)


if __name__ == '__main__':
    t1 = threading.Thread(target=func, args=(15, 20))
    t1.start()
    t1.join(5)
    t2 = threading.Thread(target=func, args=(5, 10))
    t2.start()
    t2.join()
    # 151617181956789