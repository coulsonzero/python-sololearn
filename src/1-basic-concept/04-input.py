a = input()
a = input("请输入: ")
a, b = input().split()                  # 输入两个字符串
a, b = map(int, input().split())        # 输入两个整数（用空格隔开）
a, b = map(int, input().split(','))     # 输入两个整数（用逗号隔开）