import random

# (1,100)之间的随机整数
value: int = random.randint(1, 100)
print(value)    # 3


# 随机排序
nums: list[int] = [2, 5, 3, 1, 7, 9]
random.shuffle(nums)
print(nums)     # [9, 3, 7, 5, 2, 1]

