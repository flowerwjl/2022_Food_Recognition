#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/27 下午3:15
# Author : nishizzma
# File : Add.py

from Dao.connect import connect, close


def addFoodInformation(FoodName, Url, Ingredients, Ingredients_Pic, Steps, Steps_Pic):
    db, cursor = connect()
    table_name = 'food'

    sql = ("insert into {} (FoodName, Url, Ingredients, Ingredients_Pic, Steps, Steps_Pic) "
           "values(%s,%s,%s,%s,%s,%s)".format(table_name))

    cursor.execute(sql, (FoodName, Url, Ingredients, Ingredients_Pic, Steps, Steps_Pic))
    db.commit()
    close(db)
    print("成功加入新菜谱")


def addUserInformation(Name, Passwd, Region, Flavor=None, History=None):
    '''
    用户注册函数
    :param Name:注册人昵称
    :param Passwd:注册人密码
    :param Region:注册人地区
    :param Flavor:注册人口味爱好
    :param History:注册人历史搜索
    :return:用户唯一UID
    '''
    db, cursor = connect()
    tables_name = 'User'
    sql = ("insert into {} (Name,Passwd,Region,Flavor,History) "
           "values(%s,%s,%s,%s,%s)".format(tables_name))

    cursor.execute(sql, (Name, Passwd, Region, Flavor, History))
    UID = cursor.lastrowid

    db.commit()
    close(db)
    print("成功加入用户")
    return UID
