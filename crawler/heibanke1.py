
import re
from urllib import request

def getHtml(url):
	page=request.urlopen(url)
	html=page.read()
	return html.decode('utf-8')
url='http://www.heibanke.com/lesson/crawler_ex00/'
number=['']
#print(getHtml(url))
#number=re.findall(r'数字是(\d{5})',getHtml(url))
#if int(number[0])>0:
#	print(int(number[0]))
#number=re.findall(r'数字(\d{5})',getHtml(url))
while True:
	content=url+number[0]
	number=re.findall(r'<h3>.*?(\d{5}).*?</h3>',getHtml(content))
	#print(getHtml(content))
	if not number:
		break
	else:
		print(int(number[0]))
		#print(url)
print(getHtml(content))
	
	
	
	
