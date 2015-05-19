#coding:utf-8
__author__ = 'maxbon'
#导入模块
from sys import argv

#指定参数
script, filename = argv

#打印提示
print "We're going to erase %r." % filename
print "If you don't want taht, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#提示并接收输入
raw_input("?")

#以可写权限打开文件<如不存在则创建>
print "Opening the file..."
target = open(filename, 'w')

#清空文件
print "Truncating the file.  Goodbye!"
target.truncate()

#提示
print "Now I'm going to ask you for three lines."

#输入要写入的内容
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#提示
print "I'm going to write there to the file."

#通过open的.write方法写入内容
target.write(line1+"\n"+line2+"\n"+line3+"\n")

#提示并关闭文件
print "And finally, we close it."
target.close()
