#coding:gbk
import requests as rq
url='http://www.heibanke.com/lesson/crawler_ex01/'

for i in range(1,31):
	parms={'username':'heibanke','password':str(i)}
	r=rq.post(url,data=parms)
	if r.text.find("错误")>0: #用gbk编码则支持中文，utf-8不行（不知道原因）！！！！！！！
		print ("密码", i, "错误")
	else:
		print(r.text)
		break