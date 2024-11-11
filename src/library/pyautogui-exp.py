"""
win+R --->>> cmd
1.python -m pip install pypiwin32
2.pip install pyautogui
3.pip install pillow (图片定位）
4.pip install pyinstaller   （打包成exe）
5.pip install opencv-python   （confidence识别）



运行程序时停止方法：
* ctrl+c
* 鼠标放到屏幕左上角



import pyautogui as pg
import time

time.sleep(5)    #准备时间
time.sleep(0.5)  #停顿时间

pg.PAUSE = 2.5    #为函数循环增延迟


获取屏幕分辨率：
pg.size()
获取位置：pyautogui.position()
pg.position()
>>> Point(x=1000, y=600)
判断坐标是否在屏幕上
pg.onScreen(x, y）
（创建while循环）实时获取位置 #cmd运行python
import pyautogui, sys
print('press ctrl-c to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'x: ' + str(x).rjust(4) +'Y: ' + str(y).rjust(4)
        print(positionStr,end = '')
        print('\b'*len(positionStr),end='',flush=True)
except KeyboardInterrupt:
    print('\n')


#2
import pyautogui
print('Press Ctrl-C to quit')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: {} Y: {}'.format(*[str(x).rjust(4) for x in [x, y]])
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
为函数循环增加延迟
pg.PAUSE = 2.5
鼠标置于屏幕左上角(坐标系原点）时显示异常
pg.FAILSAFE = True

调用鼠标点击：click（x,y,duration,button）
pyautogui.click()   #当前位置点击，默认右键（可插入button='left')
pg.click(x,y,duration=2) #先移动到（x,y)再点击
pyautogui.click(button='right') #双击
pyautogui.doubleClick()   #双击
pg.tripleClick()  #三连击
pg.rightClick()  #单击右键
pg.middleClick()  #单击中键

pg.click(clicks=6, interval=0.4) #多次连击
pg.click(pg.locateCenterOnScreen('.png'))  #截图定位再点击，图片需放于桌面，不能放于文件夹内
#无法点击软件按钮 ——改为 “用管理员权限”

程序暂停
os.system('pause')   #任意键推出
input()            #enter推出
time.sleep()   #等待
鼠标移动：moveTo（x,y,duration,button）


pg.moveTo(x,y,time)
pg.moveTo(x,y,t,button='left')   #从移动到指定位置
pg.dragTo(x,y)  #拖动
pg.scroll()   #滚动
pyautogui.FAILSAFE = False    #禁止鼠标在左上角
键盘操作：（str/list,interval)   #interval为每次输入间隔时间
pg.typewrite()   #输入内容
pg.hotkey()      #快捷键
pg.press(）      #按下并松开
pg.keyDown()     #按住
pg.keyUp()       #松开
pg.PUASE=1       #每隔1s执行一个操作指令
pg.write('hello python !', interval=0.3)   #控制键盘输入，interval间隔输入字符时间


弹窗
pg.alert(text='是否确认运行程序’, title='请求框',button='OK')                           #消息提醒框
pg.confirm(text='welcome to my world !', title='WeChat', buttons=['OK','Cancel'])     #选择框
pg.prompt(text='请输入您的开机密码', title='输入框', default='0627***')                 #内容输入框（可看到输入的内容）
pg.password(text='开机密码', title='消息框',default='密码', mask='*')                  #密码输入框（隐藏输入的内容）
图像操作
pg.screenshot(path)   #全图截屏
pg.screenshot(r'C:\Users\21059\Desktop\Tips\01.png'，region=(0,0,300,400)）   #区域截屏（左上角坐标，宽，高）
pg.screenshot(path, getpixel(x,y))     #获取屏幕坐标RGB颜色#无法使用
positionStr = ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(3) + ')'

pg.locateOnScreen('a.png')                #返回图片坐标位置（x,y,宽.高)
    print ("该图标在屏幕中的位置是：X={},Y={}，宽{}像素,高{}像素".format(x,y,width,height))
pg.locateCenterOnScreen()                   #返回中心坐标
for i in pg.locateAllOnScreen('a.png'):        #寻找所有相似图片
    print(i)
pg.center((x,y,w,h))   #获取图标的中心点
pg.doubleClick(pg.locateCenterOnScreen(r'path_filename.png", grayscale=False, confidence=0.7))  #pip install opencv-python以定位图片信息屏幕位置并点击
if ... != None
    print("找到图")
    time.sleep(random.randint(2,5))
else:
    print("unfind")
    time.sleep()


软件交互
import win32con
import win32clipboard as w


def get_text():
    # 读取剪切板
    w.OpenClipboard()
    t = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    a = t.decode('ANSI')  #部分文本需要这个解码，显示中文
    return a


自动循环案例1
from pymouse import PyMouse
import time
from pykeyboard import PyKeyboard


def del_all():
    # 清空文本框
    k.press_key(k.control_key)  
    k.tap_key('A')  
    k.release_key(k.control_key)
    k.tap_key(k.delete_key)


    
def click_and_type(word):
    time.sleep(0.5)
    m.click(536, 531, 1)#点击“单位列表”
    time.sleep(0.5)
    del_all()
    k.type_string(word)#输入单位编码
    time.sleep(1)
    k.tap_key(k.entry_key,1)#等它感应到对应单位后回车
    time.sleep(0.5)
    m.click(1121, 732, 1)#点击“数据采集”
    time.sleep(10)#等待数据采集完毕，一般3秒左右完成，但需要预留多一点时间确保
    m.click(1119,738,1)#点击“上一步”


#主体执行部分


list_num=['A1002002','B213212']#实际执行过程中有500多个单位，这里只展示两个


m = PyMouse()
k = PyKeyboard()


m.click(1600, 900, 1)#显示桌面
time.sleep(0.5)
m.click(324, 872, 1)#显示软件


for i in range(len(list_num)):
    word = list_num[i]
    click_and_type(word)



案例2
import pyautogui
for i in range(2, 11):
    用0.5 秒的时间把光标移动到(400, 175 + i * 20) 位置
pyautogui.moveTo(400, 175 + i * 20,
    duration = 0.5)
pyautogui.click(clicks = 2, button =
    'left', interval = 0.05)# 点击进入单据
time.sleep(3)
pyautogui.click(100, 140)# 点击修改
time.sleep(3)
pyautogui.click(350, 190, button =
    'left')# 左击发货日
pyautogui.click(350, 190, button =
    'right')# 右击发货日
time.sleep(1.5)
pyautogui.click(595, 397)# 选择日期5
time.sleep(1.5)
pyautogui.click(815, 472)# 完成
time.sleep(1.5)
pyautogui.click(565, 425)# 发出日大于接收日， 是
time.sleep(1.5)
pyautogui.click(155, 140)# 点击保存
time.sleep(2)
pyautogui.click(432, 140)# 点击查询
time.sleep(5)


每隔10s打印一次"hello,world"

#模板
from threading import Timer
def func():
    pass
class RepeatingTimer(Timer):
    def run(self):
        while not self.finished.is_set():
        self.function(*self.args, **self.kwargs)
        self.finished.wait(self.interval)
        t = RepeatingTimer(10.0,func)

t.start()




from threading import Timer
def hello():
print "hello, world"
class RepeatingTimer(Timer):
def run(self):
while not self.finished.is_set():
self.function(*self.args, **self.kwargs)
self.finished.wait(self.interval)


t = RepeatingTimer(10.0, hello)
t.start()


from threading import Thread
def hello():
print "hello, world"
# 继承 Thread
class MyThread(Thread):
# 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
def run(self):
hello()
t = MyThread()
t.start()


class _Timer(Thread):
    # Call a function after a specified number of seconds:
    #         t = Timer(30.0, f, args=[], kwargs={})
    #         t.start()
    #         t.cancel() # stop the timer's action if it's still waiting


    def __init__(self, interval, function, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()

    def cancel(self):
        # Stop the timer if it hasn't finished yet
        self.finished.set()

    def run(self):
        self.finished.wait(self.interval)
        if not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
        self.finished.set()




得到一个返回值
#path_clicked={1: {'x': 550, 'y': 856, 'button': 'Button_left', 'click_count': 1, 'time_interval': 0}, 2: {'x': 603, 'y': 853, 'button': 'Button_left', 'click_count':
1, 'time_interval': 1.53}, 3: {'x': 781, 'y': 853, 'button': 'Button_left', 'click_count': 1, 'time_interval': 2.32},
4: {'x': 871, 'y': 853, 'button': 'Button_left', 'click_count': 1, 'time_interval': 1.54}, 5: {'x': 983, 'y': 852, 'button': 'Button_left', 'click_count': 1, 'time_interval': 2.25},
6: {'x': 1087, 'y': 855, 'button': 'Button_left', 'click_count': 1, 'time_interval': 1.52}, 7: {'x': 923, 'y': 907, 'button': 'Button_left', 'click_count': 1, 'time_interval': 12.87}}

"""



'''
记录了鼠标的所有行为,前面的序列号 1 2 3..是鼠标点击次数,每次点击会记录下点击的位置 x y值,button左键还是右键点击,click_count点击次数,time_interval相邻两次点击的时间差.  这样基本上就可以完全模拟一个鼠标的所有操作.
下面是完整代码
'''

'''
import time
from pynput import mouse
from  pynput.mouse import Button
click_time=[]
click_location=[]
click_count=1
path_clicked={}
time_difference=0
count=1
def on_click(x, y , button, pressed):
    if pressed:  #点击时为ture  如果不进行判断会调用两次这个函数 一次点击一次释放 这里不需要两次
        global count
        global click_count
        global time_difference  #把时间差设为全局变量 为的是退出这个循环
        #global t
        path_infor={}
        t=time.time()
        click_time.append(t) #添加时间
        click_location.append((x,y)) #添加位置
        #print('what happend')
        if len(click_location)!=1:  #这几个判断以及上面定义的click_ 都是为了得到双击还是单击  两个list长度都是2 第一个和第二个比较时间差
            time_difference=click_time[1]-click_time[0]  #定义时间差
            print(time_difference)
            if click_location[0]==click_location[1]:
                if time_difference<=0.3:  #如果两次点击时间小于0.3秒就会判断为双击 否则就是单击
                    click_count=2
                else:
                    click_count=1
            else:
                click_count=1
            click_time.pop(0)  #删去第一个
            click_location.pop(0)
            if click_count == 2:   #双击时 第一次击中的记录需要删去 否则执行的时候会是单击即使两个单击时间间隔很短 还有时间记录的得是上一次的
                time_difference = path_clicked[count-1]['time_interval']
                count=count-1
        if button == Button.left:  #判断左键还是右键还是中键
            button_name = 'Button_left'
        elif button == Button.middle:
            button_name = 'Button_middle'
        elif button == Button.right:
            button_name = 'Button_right'
        else:
            button_name = 'Unknown'
        path_infor['x']=x
        path_infor['y']=y
        path_infor['button']=button_name
        path_infor['click_count']=click_count
        path_infor['time_interval']= round(time_difference,2)
        print('{0} Pressed at {1}  点击次数{2}'.format(button_name, (x, y),click_count))
        path_clicked[count]=path_infor
        print(path_clicked)
        count=count+1
    # else:
    #     print('{0} Released at {1} at {2} 点击次数{3}'.format(button_name, x, y,click_count))
    if not pressed:
        return False
def get_path_clicked():
    while True:  # no_move = on_move,on_click = on_click,on_scroll = on_scroll,on_move 不需要scroll只能记录方向没用
        with mouse.Listener( on_click = on_click) as listener:
            listener.join()
        if time_difference>=10:
            if input('是否继续（y or n）')=='n':
                return path_clicked
                #break
if __name__=='__main__':
    print(get_path_clicked())

'''



'''
pynput这个库无法判断点击次数,所以我就使用两次点击的时间差,来判断是点击还是双击,并当无操作十秒后提示是否继续.
运行程序后,直接进行想要重复进行的操作,然后会得到一个上面提到的path_clicked字典
再对这个字典进行解析.循环即可达到循环操作的效果,如果感觉太慢也可以再去修改时间 ,不过建议不要太快毕竟这是模拟鼠标操作不是用接口操作.
'''


'''
from pynput.mouse import Button, Controller
import time
from pynput_text import *
mouse = Controller()
path_clicked=get_path_clicked()
print(len(path_clicked))
#os.system('netease-cloud-music')
for count in range(1,len(path_clicked)):
    path_infor=path_clicked[count]
    print(path_infor)
    time.sleep(path_infor['time_interval'])
    mouse.position=(path_infor['x'],path_infor['y'])
    if path_infor['button']=='Button_left':
        mouse.click(Button.left,path_infor['click_count'])
    if path_infor['button']=='Button_right':
        mouse.click(Button.right,path_infor['click_count'])
    else:
        mouse.click(Button.middle,path_infor['click_count'])
'''