#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/27 下午3:15
# Author : nishizzma
# File : Delete.py

from Dao.connect import connect, close


def DeleteFood(id):
    db, cursor = connect()
    tables_name = 'food'
    cursor.execute("delete from %s where id='%d' " % (tables_name, id))
    db.commit()
    close(db)
    print("该食物数据已删除成功")


def DeleteUserInformation(UID):
    db, cursor = connect()
    tables_name = 'User'
    cursor.execute("delete from %s where UID='%s' " % (tables_name, UID))
    db.commit()
    close(db)
    print("该数据已删除成功")
