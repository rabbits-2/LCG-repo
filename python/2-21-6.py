#!/usr/bin/env python
#coding=utf-8

#for循环，

import sys

print sys.getdefaultencoding()

counter = 0 

while counter < 11:
	print 'loop #%d' %(counter)
	counter += 1

for num in xrange(11):
	print num

Number = int(raw_input(unicode('请输入一个数字:','utf-8').encode('gbk')))
if Number > 0:
	print u'%s 是正数' %(Number) # 增加U，可以输出中文， 
elif Number < 0:
	print u'%s 是负数' %(Number)
elif Number == 0:
	print u'%s 是 0' %(Number)
else:
	print '1'