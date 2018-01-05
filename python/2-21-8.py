#!/usr/bin/env python
#coding:utf-8

#循环和操作符

# a = raw_input(unicode('请输入5个数字:','utf-8').encode('gbk'))

# alist = [1,2,3,4,5]
b=0
i=0
while i < 5:
	b += int(raw_input(unicode('请输入1个数字:','utf-8').encode('gbk')))
	i += 1
print b 

opc = 0
for x in range(5):
	opc += int(raw_input(unicode('请输入1个数字:','utf-8').encode('gbk')))
print opc