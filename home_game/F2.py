# -*- coding:utf-8 -*-
__author__ = 'maxbon'
import status
import F1

# 阳台
def room11():
    print '你看到了一片阳台，请选择是回二楼堂屋还是结束浏览：'
    print '''1、回二楼堂屋
    2、结束浏览'''
    choose = int(raw_input('请选择1或2：'))
    if choose == 1:
        room10()
    elif choose == 2:
        status.over()
    else:
        status.dead()

# 二楼堂屋
def room10():
    print '你来到了二楼堂屋，这里有三扇门<前、左、右>，请选择：'
    print '''1、开启前门
    2、开启左门
    3、开启右门
    4、回去厨房
    5、结束浏览'''
    choose = int(raw_input('请选择1-4：'))
    if choose  == 1:
        room11()
    elif choose == 2:
        room8()
    elif choose == 3:
        room9()
    elif choose == 4:
        F1.room5()
    elif choose == 5:
        status.over()
    else:
        status.dead()

# 卧室
def room9():
    print '你来到了卧室，里面有一张很大的床，墙上贴着很多海报，请选择：'
    print '''1、回去二楼堂屋
    2、结束浏览'''
    choose = int(raw_input('请选择1-2：'))
    if choose == 1:
        room10()
    if choose == 2:
        status.over()
    else:
        status.dead()

# 书房
def room8():
    print '你来到了书房，里面有一个大书架，上面有很多书，请选择：'
    print '''1、回去二楼堂屋
    2、结束浏览'''
    choose = int(raw_input('请选择1-2：'))
    if choose == 1:
        room10()
    if choose == 2:
        status.over()
    else:
        status.dead()