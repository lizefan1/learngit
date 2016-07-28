#conding: utf-8
import requests as rq
import re
from bs4 import BeautifulSoup

def geturls(url):
    html=rq.get(url).text
    soup=BeautifulSoup(html,'html.parser')
    c=[]
    list=soup.findAll('img',changedsize="true")
    for i in list:
        c.append(str(i.attrs['src']))
    #print(len(c))
    #print(soup.prettify())
    #for j in c:
     #    print(i.attrs['src'])
    return c
	
url='http://tieba.baidu.com/p/4658874020'


j=1
for i in geturls(url):
	jpg=rq.get(i).content
	open(str(j)+'.jpg','wb').write(jpg)
	j+=1
"""
#geturls(url)
#for i in u[0]:
 #       print(u)
        
#print('url',len(geturls(url)),geturls(url)[0:5])
"""
	
