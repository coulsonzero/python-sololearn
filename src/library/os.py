'''
import os


os.chdir(path)         #更改为当前工作目录
print(os.getcwd())     #获取当前工作目录

# 创建目录
os.mkdir(path)                    #当前目录下创建子目录
os.makedirs(path1/path2/...)      #当前目录下创建多级子目录   ./指上一级目录

# 删除目录
os.rmdir(path)
os.removedirs(path1/path2/...)

# 遍历目录树
os.walk(path)
os.listdir(path)

------------------------------------------------
# 打开exe文件
os.startfile(path)
# 删除文件
os.remove(path)
# 重命名文件（移动）
os.rename(src, dst)    #只能在当前工作目录下完成！
// shutil.move()
'''


'''
import os
import os.path

# 判断：绝对路径、是否目录、是否文件、指定路径文件是否存在
print(os.path.isabs(path))
print(os.path.isdir(path))
print(os.path.isfile(path))
print(os.path.exists(path))


# 获取文件基本信息
print(os.path.getsize(filename))           # 文件大小
print(os.path.abspath(path))               # 文件绝对路径
print(os.path.dirname(p))                  # 目录路径
print(os.path.getatime(filename))          # 返回文件最后访问时间
print(os.path.getmtime(filename))          # 返回文件最后修改时间
print(os.path.walk(top,func,arg))          # 递归遍历目录
print(os.path.join(path,*paths))           # 连接多个路径
print(os.path.split(path))                 # 对路径分割
print(os.path.splitext(path))              # 从路径中分割文件的扩展名
'''
import os
if __name__ == '__main__':
    print(os.getcwd())  # 获取当前工作目录