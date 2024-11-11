'''
pythonic编程技巧



print(f"该商品价格为：{price+1:.2f}")

3. Yield 语法(Yield Statement)

# 列举斐波那契数列前n的和
def fibonacci(n):
    a, b = 0, 1
    # nums = []
    for _ in range(n):
        # nums.append(a) -->> yield a
        yield a    # 立即输出，无需等待加载完毕再输出(极大减少程序耗时)
        a, b = b, a+b
    # return nums

for i in fibonacci(10):
    print(i)


4. 列表解析式(List Comprehension)

files = ['a.py', 'b.docx', 'c.txt', 'm.py', 'uio.py', 'date.txt']
new_files = []
for f in files:
    if f.endswith('py'):
        new_files.append(f)

print(new_files)
------------------------------------------------------------------
files = ['a.py', 'b.docx', 'c.txt', 'm.py', 'uio.py', 'date.txt']
new_files = [x for x in files if x.endswith('py')]

print(new_files)


5. Enumerate 函数(Enumerate Function)

files = ['a.py', 'b.docx', 'c.txt', 'm.py', 'uio.py', 'date.txt']
# for i in files:
#    print(i)
for i, x in enumerate(files):    # (i)索引,(x)内容
    print(i, x)

>>>
0 a.py
1 b.docx
2 c.txt
3 m.py
4 uio.py
5 date.txt


6.1 反向遍历(Looping Backwards)

files = ['a.py', 'b.docx', 'c.txt', 'm.py', 'uio.py', 'date.txt']
for i, x in enumerate(reversed(files)):
    print(i, x)

6.2 按顺序排序(Looping in Sorted Order)

files = ['a.py', 'b.docx', 'c.txt', 'm.py', 'uio.py', 'date.txt']
for i, x in enumerate(sorted(files)):
    print(i, x)


7. 字典的合并操作(Dictionary Merging)
a = {"coulson": "123456", "shville": "abc123"}
b = {"tom": "123", "john": "12345"}

c = {}
for k in a:
    c[k] = a[k]
for k in b:
    c[k] = b[k]
-----------------------------------------------
c = {**a, **b}    # 解包

8. 三元运算符(Ternary Operator)
if score > 60:
    s = "pass"
else:
    s = "fail"
-----------------
s = "pass" if score > 60 else "fail"

9. 序列解包(Sequence Unpacking)
name = 'San Zhang'

str_list = name.split()
first_name = str_list[0]
last_name = str_list[1]

first_name, last_name = name.split()

10. With 语句(With Statement)
f = open("somefile.txt", "r")
s = f.read()
f.close()
# 如果忘记关闭这个文件，python会一直占用这个文件的系统资源，直到程序完全退出
#对于小脚本来说不是什么事，但对于一个需要长时间在服务器里运行的程序，系统资源可能很快就被吃光，然后程序崩溃
with open('somefile.txt','r') as f:
    s = f.read()    #with之后的语句执行完毕后文件会自动关闭，不用手动调用close（）了

http://repl.it/(在线python开发环境)

'''