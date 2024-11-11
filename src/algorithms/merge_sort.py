# 递归法对随机数组排序
import time
import random




def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
#     return merge(left, right)
#
# def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


if __name__ == '__main__':
    start = time.time()

    # nums = []
    # for i in range(20000):
    #     nums.append(random.randint(1, 50000))    >>> 300ms
    # nums = sorted(nums)

    new_nums = sorted([random.randint(1,50000) for i in range(20000)])
    new_nums = merge_sort(new_nums)
    print(new_nums)
    end = time.time()
    print(f'cpu执行用时: {(end - start) * 1000:.3f} ms')


# >>> 139 ms/0.14s     (20_000个元素时)
# 32s （冒泡迭代法用时）
# >>> 5668.777ms/5.67s (200_000个元素时)