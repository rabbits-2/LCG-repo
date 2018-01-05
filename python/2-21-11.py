#!/usr/bin/env python
#coding:utf-8

#带文本菜单的程序

while 1:                          #while一直循环遇到break跳出循环
	print u"(1)取5个数的和"
	print u"(2)取5个数的平均值"
	print u"(x)退出"
	option = raw_input(unicode('请选择序号: ','utf-8').encode('gbk'))
	if option == '1':  # '1'和1不一样带''是字符，不带的是数字，不是一种属性
		sum1 = 0
		for x in range(5):
			sum1 += int(raw_input(unicode('请输入1个数字:','utf-8').encode('gbk')))
		print u"5个数的和:",sum1
		break  
	elif option == '2':  
		aveage=0
		for x in range(5):
			aveage += float(raw_input(unicode('请输入1个数字:','utf-8').encode('gbk')))
			res = aveage/5
		print u"5个数的平均值是:",res
		break  
	elif option == 'x':
		print u"(x)退出" 
		break 
	else:
		print u"请重新选择" 