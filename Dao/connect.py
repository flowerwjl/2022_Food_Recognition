#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/16 下午7:04
# Author : nishizzma
# File : connect.py

"""
连接MySQL数据库
"""

import pymysql
import configparser


def connect():
    """
    :return:    数据库(db)，游标对象(cursor)
    """

    CONFIG_PATH = '../config.ini'
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    host = config["DATABASE"]["HOST"]
    port = config["DATABASE"]["PORT"]
    user = config["DATABASE"]["USER"]
    passwd = config["DATABASE"]["PASSWD"]
    database = config["DATABASE"]["DB"]

    db = pymysql.connect(
        host=host,
        port=int(port),
        user=user,
        passwd=passwd,
        db=database,
        # charset='utf8'
    )

    # 使用cursor()方法创建一个游标对象cursor
    cursor = db.cursor()
    return db, cursor


def close(db):
    """
    :param db:  待关闭数据库
    """
    db.close()
