import tkinter as tk

window = tk.Tk()            # 1.创建窗口变量"window"，可改为"root"
window.title('My window')   # 2.窗口命名
window.geometry('500x300')  # 3.设定窗口大小（'500x300+200+100')     注意：x字母不是乘*

window.mainloop()           # 5.主窗口循环显示，没有则不显示窗