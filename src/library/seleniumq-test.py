from selenium import webdriver

# 初始化浏览器为chrome浏览器
browser = webdriver.Chrome()
# 访问百度首页
browser.get(r'https://www.baidu.com')
# 关闭浏览器
browser.close()
