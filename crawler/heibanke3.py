#coding:gbk
from selenium import webdriver
import time
#用test账号登入。密码test123
driver=webdriver.Firefox()
driver.get('http://www.heibanke.com/lesson/crawler_ex02/')
driver.find_element_by_id('id_username').send_keys('test')
driver.find_element_by_id('id_password').send_keys('test123')
driver.find_element_by_id('id_submit').click()
time.sleep(3)
for i in range(1,31):
	driver.get('http://www.heibanke.com/lesson/crawler_ex02/')
	driver.find_element_by_name('username').send_keys('lzf')
	driver.find_element_by_name('password').send_keys(i)
	driver.find_element_by_id('id_submit').click()
	time.sleep(2)
	if driver.page_source.find('错误')>0:
		print('wrong',i)
	else:
		print(driver.page_source)
#driver.close()