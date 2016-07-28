import easygui as g
msg='【真实姓名】 必填项\n【手机号码】 必填项\n 【E-mail】 必填项'
title='账号中心'
fields=['*用户名', '*姓名', '*手机号码', 'QQ', 'E-mail']
fieldValues=g.multenterbox(msg,title,fields)
print(fieldValues)
while 1:
	if fieldValues==None:
		break
	err=''
	for i in range(len(fields)):
		option=fields[i].strip()
		if fieldValues[i].strip()=='' and option[0]=='*':
			err+=('[%s]为必填 \n' %fields[i])
	if err=='':
		break
			
	fieldValues=g.multenterbox(err,title,fields,fieldValues)
print('用户资料如下: %s' % str(fieldValues))

