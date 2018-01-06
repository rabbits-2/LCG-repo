#!/usr/bin/env python
#coding:utf-8

#列表和元组

aList = [1,2,3,4]  #列表用[] 表示

print aList

print aList[0]

print aList[2:]   #列表可以切片，

print aList[:3]

aList[1] = 5  # 

print aList


aTuple = ('robots',78,93,'try')  #元组用()表示，

print aTuple                    #元组可以切片，

print aTuple[:3] 

print aTuple[0]   

# aTuple[1] = 5   #元组可以切片，但是其中的元素不可以修改，

aDict = {'host':'earth','dns':'127.0.0.1'}  #字典元素放在{}中，键-值对象

print aDict

aDict['port'] = 80

print aDict

# aDict.key()

print aDict['port']

for key in aDict:
	print key ,aDict[key]



