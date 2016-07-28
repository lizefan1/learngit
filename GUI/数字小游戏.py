import random,sys
import easygui as g
n=random.randint(1,10)
while 1:
	try:
		user_n=int(g.integerbox(msg='猜下我想到的数字(1-10):',title='数字小游戏',lowerbound=1,upperbound=10))
	except NameError:
		print('请输入数字')

	if user_n > n:
		print('大了一点')
		g.msgbox(msg='大了一点', ok_button='再猜一次')
		#break
	elif user_n < n:
		print('小了一点')
		g.msgbox(msg='小了一点', ok_button='再猜一次')
		#break
	else:
		print('猜对了')
		g.msgbox(msg='猜对了')
		g.msgbox(msg='猜中了也没奖励')
		break
g.msgbox(msg='游戏结束了')




