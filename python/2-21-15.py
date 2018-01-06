#!/usr/bin/env python
#coding:utf-8

#输入3个数字，然后按照从大到小的顺序排列出来，
a=raw_input('Enter a number:')
b=raw_input('Enter a number:')
if a<b:
	tmp=a
	a=b
	b=tmp
c=raw_input('Enter a number:')
if a<c:
	tmp=a
	a=c
	c=tmp
if b<c:
	tmp=b
	b=c
	c=tmp
print a,b,c

#!/usr/bin/env python
#coding:utf-8

#输入3个数字，然后按照从小到大的顺序排列出来，
aa=raw_input('Enter a number:')
bb=raw_input('Enter a number:')
if aa>bb:
	tmp=aa
	aa=bb
	bb=tmp
cc=raw_input('Enter a number:')
if aa>cc:
	tmp=aa
	aa=cc
	cc=tmp
if bb>cc:
	tmp=bb
	bb=cc
	cc=tmp
print aa,bb,cc