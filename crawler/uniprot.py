#coding:UTF-8
import requests as rq
import re
url1='http://www.uniprot.org/uniprot/?query='
url2='&sort=score'
url3='keratin' #相应的uniprot检索词条，可以通过循环语句得到。
url=url1+url3+url2 #组合好的检索网址
r=rq.get(url).text 
print(url)
#print(r) #打印会出现编码错误！
#正则表达式搜索出蛋白相应的entry项目
a=re.findall(r'</script></td></tr></thead><tbody><tr id="(.*?)" class',r)
print(a[0])
