import numpy as np

'''
x = np.array(...)
x = np.arange(...)
x.reshape(6)

np.append(x, ...)
np.sort(x)

np.sum(x)
np.mean(x)
np.median(x)
np.var(x)
np.std(x)
'''

def numpy_array():
    # np.array()
    x = np.array([1, 2, 3, 4])
    print(x[0])     # 1

    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(x[1][2])  # 6

    x = np.array([2, 1, 3])
    x = np.append(x, 4)
    x = np.append(x, 0)
    x = np.append(x, [6, 7, 5])
    x = np.sort(x)

    print(x)    # [0 1 2 3 4 5 6 7]

def numpy_arange():
    x = np.arange(1, 7)     # [1 2 3 4 5 6]
    print(x)

    x = np.array([[1, 2], [3, 4], [5, 6]])
    z = x.reshape(6)        # [1 2 3 4 5 6]
    print(z)

def numpy_slice():
    x = np.arange(1, 10)
    print(x[0:2])   # [1, 2]
    print(x[5:])    # [6, 7, 8, 9]
    print(x[:2])    # [1, 2]
    print(x[-3:])   # [7, 8, 9]
    print(x[1:5:2]) # [2, 4]

    print(x[x<4])   # [1, 2, 3]
    print(x.sum())  # 45

def numpy_statistic():
    x = np.array([14, 18, 19, 24, 26, 33, 42, 55, 67])
    print(np.mean(x))       # 33.111111111111114
    print(np.median(x))     # 26.0
    print(np.var(x))        # 292.5432098765432
    print(np.std(x))        # 17.10389458212787


if __name__ == '__main__':
    pass