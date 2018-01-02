#!/usr/bin/env python
#coding:utf-8

#用户输入文件名，然后打开文件，并显示他的内容到屏幕上，

filename = raw_input('Enter your name: ')
fobj = open(filename,'r')
for eachLine in fobj:
	print eachLine,
fobj.close()
