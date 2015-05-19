# coding:gbk
# It's a Test Script to read test.txt
__author__ = 'maxbon'

from sys import argv

script, filename = argv
txt = open(filename)

print "打开%s文件。。。" % filename
print txt.read()
txt.close()

open_again = raw_input("请输入文件名再次打开文件：")
txt_again = open(open_again)

print "%s文件内容如下：" % open_again
print txt_again.read()

print "关闭文件。。。"
txt_again.close()
