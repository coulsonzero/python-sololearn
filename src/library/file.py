"""
f = open(filepath, mode, encoding='utf-8'):
    ...)
f.close()


with open(filepath, mode, encoding) as fp:
    s = fp.read()    # s = ''.join(fp.readlines())



# 快速遍历大型文件
with open(filename,"rb") as f:
    for line in f:
        pass


filepath：
[x]r'C:\Users\21059\Desktop'    --->>> 原始字符串
[x]'C:\\Users\\21059\\Desktop'  --->>> 转义字符串
[x]'.\\....txt'                 --->>> 当前路径文件


mode：
* r  只读      (文件不存在报错/文件必须存在)
* x  创造写入  (文件存在报错)
* w  重写      (文件不存在新建)
* a  追加(写入)(文件不存在新建)
* b  二进制(配合其他mode使用)
* +  读写(配合其他mode使用，不能单独使用)
遍历用'rb'最快！


File Methods：
#读取
read()                 # 读取所有文本/指定数量文本,返回str
readline()             # 读取一行文本
readlines()            # 读取每行文本，返回list(r+直接读取；w+/a+则需要加fp.seek(0)才可读取)
readable()

# 写
write()
write(','.join((name,password)))
writelines( <List> )
writeable()



# 查找
seek(offset,whence)
tell()                #光标当前位置,返回int字节
truncate( <size> )    #删除从当前指针位置到文件末尾的内容
#偏移量int字节，whence=0:文件开头(默认)；1为当前位置；2为文件结尾
#除默认模式外whence=1 or 2，要用带二进制b的打开方式使用


# 保存(关闭)
close() --- 关闭(保存)
flush() --- 刷新(保存但不关闭)

"""