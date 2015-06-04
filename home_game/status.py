# -*- coding:utf-8 -*-
__author__ = 'maxbon'

from sys import exit
import F1

# 挂了
def dead():
    print '你选择了没有的，你挂了。。游戏结束'
    exit(0)

# 结束参观
def over():
    print '谢谢参观，欢迎下次光临。'
    exit(0)

# 开始
def start():
    print '开始参观之旅吧'
    F1.room1()