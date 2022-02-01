#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/27 下午2:54
# Author : nishizzma
# File : Register.py

from Dao.Add import addUserInformation
from UserSystem.md5Use import get_md5

def addUser(Name, Passwd, Region, Flavor, History):
    Passwd = get_md5(Passwd)
    UID = addUserInformation(Name, Passwd, Region, Flavor, History)
    print("恭喜创建用户成功，唯一UID:{}".format(UID))
    return UID
