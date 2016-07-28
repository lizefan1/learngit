from selenium import webdriver
import time
#driver=webdriver.Firefox()
driver=webdriver.PhantomJS(executable_path='E:\\phantomjs\\bin\\phantomjs')
driver.get('http://www.baidu.com')
driver.find_element_by_name("tj_login").click()
driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys("lizefan1")
driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('a19910108')
driver.find_element_by_id("TANGRAM__PSP_3__submit").click()
