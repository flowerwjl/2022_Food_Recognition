#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/22 下午7:48
# Author : nishizzma
# File : main.py
"""
用于测试整个代码的主函数
"""
from Dao.query import *
from FoodRecongnition.RequestFoodName import FoodNameSearch


def main_method(filepath):
    # 美食照片所在路径
    # FoodPic = './FoodPicture/1.jpg'
    FoodPic = filepath

    # 调用图片识别函数，返回食物名称
    FoodNames = FoodNameSearch(FoodPic)
    FoodName = FoodNames[0]
    Foodlists = ResearchFood(FoodName=FoodName)
    if len(Foodlists) == 0:
        print("未在数据库中搜索到结果！")
        exit()
    for foods in Foodlists:
        print('name:'+foods[1])
        print('url:' + foods[2])
        print('材料:' + foods[3])
        print('成品图:' + foods[4])
        print('步骤:' + foods[5])
        print('步骤图片:' + foods[6])

    for i in range(1, len(Foodlists) + 1):
        Foodlists[i-1].append(i)
    return FoodNames, Foodlists
