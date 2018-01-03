#!/usr/bin/env python
#coding:utf-8

#类的定义

class FooClass(object):
	"""my very first class:FooClass"""
	version = 0.1   #class (data) attribute
	def __init__(self, nm='John Doe'):
		"""constructor 构造器"""
		self.name = nm  #class instance (data) attribute
		print 'Created a class instance for',nm
def showname(self):
	"""display instance attribute and class name 显示实例属性和类的名称"""
	print 'Your name is ', self.name
	print 'My name is ',self.__class__.__name__
def showver(self):
	"""display class (static) attribute 显示类（静态）属性"""
	print self.version # reference（参考） FooClass.version
def addMe2Me(self, x): #does not use'self'
	"""apply + operation to argument(参数)"""
	return x + x
fool = FooClass('Bob')

print fool

print fool.showname()

print 'Enter',fool.showver()

print fool.addMe2Me(5)

print fool.addMe2Me('xyz')
