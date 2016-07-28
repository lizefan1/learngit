
import easygui as g
import os
file_path=g.fileopenbox(default='*.txt')
with open(file_path) as f:
	title=os.path.basename(file_path)
	msg='打开文件%s'%title
	text=f.read()
	text_new=g.textbox(msg,title,text) 						#按下ok 后，会有文本返回值
if text!=text_new[:-1]:											#textbox返回的文本会在最后一行加上\n的符号，所以要去掉再比较
	x=g.buttonbox('检测到文件内容变化','警告',('覆盖','放弃','另存为'))
	if x=='覆盖':
		with open(file_path,'w') as n_f:
			n_f.write(text_new[:-1])
	if x=='放弃':
		pass
	if x=='另存为':
		another_path=g.filesavebox(default='.txt')   #默认保存为 txt格式
		if os.path.splitext(another_path)[1]!='.txt':        #路径和后缀名分开，选取路径名
			another_path+='.txt'							#为文件加上后缀
		with open(another_path,'w') as new_f:
			new_f.write(text_new[:-1])
		
