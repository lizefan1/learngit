from selenium import webdriver
import time
driver=webdriver.IEDriverServer.exe()
driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.50862.754894437.1.B1UqB3&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
driver.find_element_by_id("J_Quick2Static").click()
driver.find_element_by_id('TPL_username_1').send_keys("793897372@qq.com")
driver.find_element_by_id('TPL_password_1').send_keys('qwe19910108mnb')
driver.find_element_by_id("J_SubmitStatic").click()
