#coding: 'utf-8'
import os
import easygui as g

def get_line(file): 	#获取每个文件的行数
	line=0
	#for i in filelist:
	with open(file) as f:
		try:
			for eachline in f:
				line+=1
		except UnicodeDecodeError:
			pass
	return line
            

def get_filenuber(dirpath):	#计算py文件，并返回py文件的列表
	#i=0
	filelist=[]
	for root,dirs,filenames in os.walk(dirpath):
		for filename in filenames:
				path=os.path.join(root,filename)
				if os.path.splitext(path)[1]=='.py':
					filelist.append(path)
					#get_line(path)    
					#i+=1

	return filelist

dirpath=g.diropenbox(msg='打开需要统计的文件夹',title='统计.py文件')	#打开文件夹路径
#print(dirpath)
filelist=get_filenuber(dirpath)
#统计各个文件中的代码行数综合
n=0							
for i in filelist:
	n+=get_line(i)			
#print(filelist)
#print(n)
g.msgbox('包含%s个文件，%s行代码'%(len(filelist),n),'统计结果')
                
                
                
