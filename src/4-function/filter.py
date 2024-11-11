nums: list = [3, 1, 7, 12, 6]

ans = list(filter(lambda x: x & 1 == 0, nums))

print(ans)
# [12, 6]