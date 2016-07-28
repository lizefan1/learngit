import urllib.request,urllib.parse,json,easygui,time
title='有道翻译'
msg=''
fields=['输入翻译内容','翻译结果']
fieldValues=[]
fieldValues=easygui.multenterbox(msg,title,fields)		#表格窗口
#time.sleep(1)
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'
data={}
data[type]='AUTO'
data['i']=fieldValues[0]								#输入翻译内容
data['doctype']='json'
data['xmlVersion']='1.8'
data['keyfrom']='fanyi.web'
data['ue']='UTF-8'
data['action']='FY_BY_ENTER'
data['typoResult']='true'

data=urllib.parse.urlencode(data).encode('utf-8')		#data的转码   encode?
response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')									#decode?					
#print(html)											
target=json.loads(html)									#json解码内容
print('翻译结果: %s' %(target['translateResult'][0][0]['tgt']))
fieldValues[1]=target['translateResult'][0][0]['tgt']					#翻译结果
easygui.multenterbox(msg,title,fields,fieldValues)						#再次显示表格窗口（包括翻译结果）
#print(fieldValues)