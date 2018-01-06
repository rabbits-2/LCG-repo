#!/usr/bin/env python
#coding:utf-8

print 'I Like to use the internet for: '
for item in ['e-mail','net-surfing','homework','chat']:
	print item
print

#for循环使用方法

squared = [x**2 for x in range(8) if not x % 2]
for i in squared:
	print i

square = [x**2 for x in range(8) ]
for a in square:
	print a