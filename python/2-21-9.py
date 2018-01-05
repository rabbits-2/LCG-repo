#!/usr/bin/env python
#coding:utf-8

#循环和操作符

alist = [3,2,3,1,5]
sum1=0
for x in alist:
	sum1 += float(x)
res = sum1/len(alist)
print res