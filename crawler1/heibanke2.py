#coding:gbk
import requests as rq
url='http://www.heibanke.com/lesson/crawler_ex01/'

for i in range(1,31):
	parms={'username':'heibanke','password':str(i)}
	r=rq.post(url,data=parms)
	if r.text.find("����")>0: #��gbk������֧�����ģ�utf-8���У���֪��ԭ�򣩣�������������
		print ("����", i, "����")
	else:
		print(r.text)
		break