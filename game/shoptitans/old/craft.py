"""
@date: 2021-04-13
传奇商店自动制作
"""

import pyautogui as pg
import time


# 自动制作
def craft():
    time.sleep(3)


    # 就绪？：定位
    ready = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\craft\\ready.png', grayscale=False, confidence=0.7)
    time.sleep(1)
    # 无 - 按空格 - -制作
    while ready != None:
        pg.doubleClick(pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\craft\\ready.png', grayscale=False,confidence=0.6), interval=0.3)
        print("-----制作完成-----")
        collect = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\craft\\collect.png', grayscale=False,confidence=0.7)
        time.sleep(0.5)
        if collect != None:
            print("正在收集")
            pg.click(collect, interval=0.5)
            time.sleep(0.3)
    else:
        print("未就绪")
        #秒？
        second = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\craft\\second.png', grayscale=False,confidence=0.7)
        time.sleep(1)
        print(second)
        if second != None:
            print("未发现就绪，等待10s")
            time.sleep(10)
        else:
            print("开始制作")
            pg.press('space', interval=1)
            # 定位图片
            T1 = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\craft\\T1.png', grayscale=False, confidence=0.7)
            # 点击11次
            pg.moveTo(T1, duration=0.5)
            pg.click(clicks=11, interval=1)
            print("正在制作T1")
        # # 收集？
        # collect = pg.locateCenterOnScreen(r'C:\\Users\\21059\\Desktop\\ShopTians\\craft\\collect.png',
        #                                       grayscale=False, confidence=0.7)
        # time.sleep(1)
        # if collect != None:
        #     print("正在收集")
        #     pg.click(collect, interval=0.5)
        #     time.sleep(1)




if __name__ == '__main__':
    for cr in range(30):
        craft()



