#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/28 下午2:56
# Author : nishizzma
# File : ChangePd.py
"""
修改密码
"""
from Dao.update import UpdateUserInfmation
from md5Use import get_md5
from UserSystem.LogIn import VerifyInformation


def ChangePasswd(UID, old_passwd, new_passwd):
    if VerifyInformation(UID, old_passwd):
        Passwd = get_md5(new_passwd)
        UpdateUserInfmation(UID, Passwd=Passwd)
    else:
        print("原始密码错误")
