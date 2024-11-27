from tkinter import *

root = Tk()                                      # 创建窗口

root.title("tkinter test")                       # 标题
root.geometry('500x300+200+100')                 # 初始大小和位置（'500x300+200+100')
# root.resizable(False,False)                    # 大小设置为不可更改
# root.iconphoto(True,tk.PhotoImage(file='*.png'))
root.attributes('-alpha', 0.9)                   # 半透明
root.attributes('-topmost', 1)                   # 保持顶端
# root.overrideredirect(True)                    # 不显示标题栏

root.mainloop()