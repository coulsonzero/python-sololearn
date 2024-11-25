"""
selenium webdriver爬网站资源

准备工作：
1. pip install selenium -i
2. https://npm.taobao.org/mirrors/chromedriver  /   https://chromedriver.chromium.org/downloads
3. "帮助"  查看版本
4. Chromedriver 解压后放到python解释器所在的文件夹（pycharm第一行可见）


from selenium import webdriver
from selenium.webdriver import ActionChains        #模拟鼠标操作
from selenium.webdriver.common.keys import Keys    #模拟键盘操作
import time
import random

#step 1: 声明浏览器
web = webdriver.Chrome()

#step 2: 访问网站
web.get('https://cn.bing.com/')



from selenium import webdriver
from selenium.webdriver import ActionChains        #模拟鼠标操作
from selenium.webdriver.common.keys import Keys    #模拟键盘操作




from selenium import webdriver  # pip install selenium -i
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_condition     # as EC
from selenium.webdriver.common.by import By
import time

#step 1: 声明浏览器
web/browser = webdriver.Chrome(r'...\chrome.exe')
web = webdriver.Safari()
web = webdriver.Edge()
web = webdriver.Firefox()
web = webdriver.PhantomaJS()  #无界面浏览器, 获取的截图是长图，一般浏览器为可见截图

#step 2: 访问网站
web.get('http://www.taobao.com')


#step 3: 查找定位元素方法
web.find_element(s)_by_link_text('')        #如果报错，去掉element后面的“s”
web.find_element(s)_by_xpath('')

#from selenium.webdriver.common.keys import Keys
web.find_element(s)_by_xpath('').send_keys("python", Keys.ENTER)
web.find_element(s)_by_id()
web.find_elements_by_class_name()
...

# step 4： 元素操作
.click()                   # 鼠标点击
.send_keys()               # 键盘输入与按键
.text
.get_attribute('href')

# step 5: 等待响应
time.sleep(random.randint(1, 2))
time.sleep(3)             # 强制等待
web.implicitly_wait(10)   # 隐式等待，最长10s
WebDriverWait(web, 20, 0.5).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, '词典')))   #显示等待最长20s，每0.5s检查一次，通过链接文本内容定位标签是否存在，如果20s上限就抛出异常

# 常用方法
web.save_screenshot('....png')
web.back()
web.forward()
web.close()   #关闭当前页面窗口
web.quit()
web.page_soure()
web.current_url
# 跳转窗口
web.switch_to.window(web.window_handles[-1])
# 跳转播放窗口
web.switch_to.frame(web.find_element_by_...)
# 切回
web.switch_to.default_content()


# 下拉列表
from selenium.webdriver.support.select import Select
import time

sel = Select(web.find_element_by_xpath('')
for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(2)
    table=web.find_element_by_xpath('')
    print(table.text)
web.close()

#不显示浏览器操作，只显示结果,后台运行
from selenium.webdriver.chrome.option import Options
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
web = Chrome(options=opt)

#网页鼠标点击动作
result = dic["key"]
re_list=result.split("|")
for rs in re_list:
    p_temp = rs.split(",")
    x = int(p_tem[0])
    y = int(p_tem[1])
   # 移动到某位置并以其为原点并点击ActionChains(web).move_to_element_with_offset(..., x, y).click().perform()


"""