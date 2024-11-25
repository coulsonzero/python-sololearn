def list_demo():
    nums = [1, 3, 2, 7, 4]
    print(nums[::-2])   # [4, 2, 1]
    print(nums[::2])    # [1, 2, 4]


if __name__ == '__main__':
    list_demo()