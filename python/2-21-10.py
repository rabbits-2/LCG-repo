#!/usr/bin/env python
#coding:utf-8

#带循环和条件判断的用户输入

# charstr = raw_input(unicode('请输入一个数字:','utf-8').encode('gbk'))

# while 1<x and x<100:
#	print 

while 1:                           #while 1 可以一直循环
     number=int(raw_input(unicode('请输入一个在1和100之间数字: ','utf-8').encode('gbk')))  
     if number>=1 and number<=100:  
        print u"您输入%d在1和100之间" %number  
        break  
     else:  
        print u"您输入的数字不在1和100之间，请重新输入！"  