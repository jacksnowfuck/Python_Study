# -*- coding:utf-8 -*-
__author__ = 'maxbon'
import status
import F2

# 杂物间
def room7():
    print '你来到了杂物间，里面黑黑的，堆了一些成年的船板和柜子，请选择：'
    print '''1、回去厨房
    2、结束浏览'''
    choose = int(raw_input('请选择1-2：'))
    if choose == 1:
        room5()
    if choose == 2:
        status.over()
    else:
        status.dead()

# 天井
def room6():
    print '你来到了天井，这里可以看到蓝蓝的天空，下面是一口古井，你喝了一口井水，有点甜，请选择：'
    print '''1、回去厨房
    2、结束浏览'''
    choose = int(raw_input('请选择1-2：'))
    if choose == 1:
        room5()
    if choose == 2:
        status.over()
    else:
        status.dead()

# 厨房
def room5():
    print '你来到了厨房，里面有很多吃的，厨房有三张门，请选择打开其中一扇：'
    print '''1、前门
    2、左门
    3、右门
    4、回去一楼堂屋
    5、结束浏览'''
    choose = int(raw_input('请选择1-5：'))
    if choose == 1:
        room7()
    elif choose == 2:
        F2.room10()
    elif choose == 3:
        room6()
    elif choose == 4:
        room2()
    elif choose == 5:
        status.over()
    else:
        status.dead()

# 电视房
def room4():
    print '你来到了电视房，里面有一个55英寸的大电视，正在播放新闻联播，请选择：'
    print '''1、回去一楼堂屋
    2、结束浏览'''
    choose = int(raw_input('请选择1-2：'))
    if choose == 1:
        room2()
    if choose == 2:
        status.over()
    else:
        status.dead()

# 车库
def room3():
    print '你来到了车库，里面有一辆法拉利跑车，洗得很干净，看上去很新，请选择：'
    print '''1、回去一楼堂屋
    2、结束浏览'''
    choose = int(raw_input('请选择1-2：'))
    if choose == 1:
        room2()
    if choose == 2:
        status.over()
    else:
        status.dead()

# 堂屋
def room2():
    print '你来到了一楼堂屋，堂屋很宽敞，墙上挂着一副十字绣，堂屋有三扇门，请打开：'
    print '''1、打开前门
    2、打开左门
    3、打开右门
    4、回去大门外
    5、结束浏览'''
    choose = int(raw_input('请选择1-5：'))
    if choose == 1:
        room5()
    elif choose == 2:
        room3()
    elif choose == 3:
        room4()
    elif choose == 4:
        room1()
    elif choose == 5:
        status.over()
    else:
        status.dead()

# 大门
def room1():
    print '你在大门口看了一下，考虑是否要进去参观，请选择：'
    print '''1、进去参观
    2、不进去了'''
    choose = int(raw_input('请选择1-2：'))
    if choose == 1:
        room2()
    elif choose == 2:
        status.start()
    else:
        status.dead()