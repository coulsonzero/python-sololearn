import random

def add():
    nums = [1, 2, 3, 4]  # [...]
    # 增
    nums.append(5)       # [..., 5]
    nums.insert(0, 0)    # [0, ...]
    nums.extend([6, 7])  # [..., 6, 7]
    nums += [8, 9]       # [..., 8, 9]

    print(nums, id(nums))

def remove():
    nums = [1, 2, 3, 4]
    # 删
    # nums.pop()
    # nums.pop(-1)        # 删除指定index的value
    # nums.pop(10)        # IndexError: pop index out of range

    # nums.remove(3)
    # nums.remove(7)      # ValueError: list.remove(x): x not in list

    # del nums[1:2]

    # nums.clear()      # []

def get():
    # 查
    nums = [3, "tom", "john", [1, 7], 3, 'a', 3.14, 7]
    # print(len(nums))
    # print(nums.index(3))
    # print(nums.count(2))      # ValueError: 2 is not in list

def sort():
    pass
    nums = [6, 3, 7, 0, 9]
    # nums.sort()               # [0, 3, 6, 7, 9]
    # nums.sort(reverse=True)   # [9, 7, 6, 3, 0]
    # random.shuffle(nums)      # [6, 0, 9, 3, 7]

    # nums = ['q', 'a', 'k', 'b']
    # nums.sort()               # ['a', 'b', 'k', 'q']
    # nums.sort(reverse=True)   # ['q', 'k', 'b', 'a']
    print(nums)




def iter():
    nums = ['q', 'a', 'k', 'b']
    # for i in range(len(nums)):
    #     print(i)

    # for i in nums:
    #     print(i)

    # for i, v in enumerate(nums):
    #     print(i, v)

def change():
    # 改
    nums = [1, 2, 3]

    print(nums)

def demo():
    nums = [1, 2, 3]
    print(5 in nums)    # False
    print(2 in nums)    # True


def for_list():
    nums = ['q', 'a', 'k', 'b']
    for i in range(len(nums) - 1, -1, -1):
        print(nums[i])


if __name__ == '__main__':
    # add()
    # remove()
    # get()
    # iter()
    # demo()
    # for_list()
    sort()
    pass
