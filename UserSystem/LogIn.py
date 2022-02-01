#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/28 上午11:21
# Author : nishizzma
# File : LogIn.py

"""
用户登陆验证界面
"""
from Dao.query import ResearchUser
from md5Use import get_md5

def VerifyInformation(UID,Passwd):
    '''
    进行登陆验证
    :param UID:用户唯一UID
    :param Passwd:密码
    :return:是否成功登陆
    '''

    UserInf = ResearchUser(UID)
    if Passwd == get_md5(UserInf[2]):
        print("验证成功，正在登陆ing")
        return True
    else:
        print("密码输入有误，请重新输入")
        return False
