import time
import random




def bubble_sort2(nums):
    n = len(nums)
    for i in range(n):
        for j in range(1, n-i):
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                return nums

def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    start = time.time()
    nums = []
    for i in range(2000):
        nums.append(random.randint(1,5000))
    nums = sorted(nums)
    # print(nums)
    bubble_sort(nums)
    end = time.time()
    print(f'cpu执行用时: {(end - start)*1000:.3f} ms')

# >>> 32904.290ms/32.9s
