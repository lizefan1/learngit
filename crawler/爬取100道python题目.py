# -*- coding= 'UTF-8' -*-
#爬虫抓取100道python习题 20160723
#多个##的内容为需要注意内容
from bs4 import BeautifulSoup
import requests as rq
import re
import os

def getTxt(urllit):										#传入url列表后，生成相应的txt文件
	m=1
	for url in urllist:
		page=rq.get(url).text
		soup=BeautifulSoup(page,'html.parser')			#生成soup对象
		#print(soup.prettify())
		c1=[]
		list1=soup.findAll('p')							#所有<p>的内容，组成列表
		for i in list1:
			c1.append(i.text)
			#print(i.text)
		c1.pop()										#删除最后两项 也可以用c1=c1[:-2]
		c1.pop()	
		list=soup.findAll('pre')						#所有<pre>的内容，组成列表
		for j in list:
			c1.append(j.text)
			#print(j.text)
		n=c1[1][3:12]									#n为文件命名的一部分
		table=n.maketrans('*/\:?"<>|','         ')		#### 去掉文件名中的非法字符（用空格号替换）#
		n=n.translate(table)							# 去掉文件名中的非法字符
		if not os.path.exists(str(m)+n+'.txt'):			#判断文件是否存在
			for k in c1:
				#if not os.path.exists(str(m)+n+'.txt'):
				f=open(str(m)+n+'.txt','a+',encoding='utf-8')		### 一定要用utf-8编码，否则默认的‘gbk’会出错#
				f.write(k)
				f.close()
		m+=1

def getUrl(u):								#获取url列表
	urllist=[]
	for i in range(1,101):
		urllist.append(u+str(i)+'.html')
	return urllist
	
u='http://www.runoob.com/python/python-exercise-example'
urllist=getUrl(u)
getTxt(urllist)

