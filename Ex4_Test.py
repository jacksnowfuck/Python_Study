# coding:gbk
# It's a Test Script to read test.txt
__author__ = 'maxbon'

from sys import argv

script, filename = argv
txt = open(filename)

print "��%s�ļ�������" % filename
print txt.read()
txt.close()

open_again = raw_input("�������ļ����ٴδ��ļ���")
txt_again = open(open_again)

print "%s�ļ��������£�" % open_again
print txt_again.read()

print "�ر��ļ�������"
txt_again.close()
