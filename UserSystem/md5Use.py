#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/28 下午2:51
# Author : nishizzma
# File : md5Use.py
import hashlib,random
import configparser

def get_md5(s):
    '''
    使用md5进行加密
    :param s:密码
    :return:密码在md5加盐后结果
    '''
    CONFIG_PATH = '../config.ini'
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    salt = config["Salt"]["salt"]
    s = s + salt
    return hashlib.md5(s.encode('utf-8')).hexdigest()
