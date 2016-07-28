from selenium import webdriver
import time
driver=webdriver.PhantomJS(executable_path='E:\\phantomjs\\bin\\phantomjs')
#driver=webdriver.ie(executable_path='C:\\Program Files\\Internet Explorer\\iexplore')
driver.get('https://its.pku.edu.cn/')
driver.find_element_by_id('username').send_keys("1401110380")
driver.find_element_by_id('password').send_keys('a19910108')
driver.find_element_by_name("connect").click()
driver.get_screenshot_as_file('已登录.png')
