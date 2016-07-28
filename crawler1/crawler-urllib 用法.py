#小爬虫
import re
from urllib import request

def getHtml(url):
	page=request.urlopen(url)
	html=page.read()
	return html.decode('utf-8')

getHtml('http://tieba.baidu.com/p/4619062407')

print(getHtml)