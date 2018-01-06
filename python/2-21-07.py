#!/usr/bin/env python
#coding:utf-8

#循环和字符串

charstr = raw_input(unicode('请输入一个数字:','utf-8').encode('gbk'))
i = 0 
while i< len(charstr):
	print charstr[i]
	i += 1

for x in charstr: #for遍历charstr中的每个元素，
	print x
