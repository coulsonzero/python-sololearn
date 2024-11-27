from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

def spider(url, keyword):
    web = webdriver.Chrome()    # step 1: 初始化浏览器
    web.get(url)
    web.implicitly_wait(3)      # 隐式等待3s--确保内容加载完全

    # 定位元素
    input_tag = web.find_element(By.ID, 'key')
    input_tag.send_keys(keyword)    # 模拟键盘输入关键字
    input_tag.send_keys(Keys.ENTER) # 模拟键盘按Enter键
    time.sleep(random.randint(2, 5))
    print(input_tag)


if __name__ == '__main__':
    spider(url='https://www.jd.com', keyword="口罩")
