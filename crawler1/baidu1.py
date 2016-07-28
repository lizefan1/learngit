#conding: utf-8
import requests as rq
import re

def geturls(url):												#返回该网址中图片的url链接列表
	html=rq.get(url).text
	pattern=re.compile(r'src="(.*?jpg)" changedsize')			#匹配图片链接
	r=re.findall(pattern,html)
	urls=[]
	for i in r:
		urls.append(i)
	return urls



#def download ()
	


url='http://tieba.baidu.com/p/4658874020'
"""
j=0
for i in geturls(url):
	jpg=rq.get(i).content
	open(str(j)+'.jpg','wb').write(jpg)					#保存图片
	j+=1
"""
u=geturls(url)
for i in u:
        print(i)
print(len(c))
#print('url',len(geturls(url)),geturls(url)[0:3])
	
