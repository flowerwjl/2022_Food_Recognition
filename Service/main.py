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


if __name__ == '__main__':
    # 美食照片所在路径
    FoodPic = './FoodPicture/1.jpg'

    # 调用图片识别函数，返回食物名称
    FoodNames = FoodNameSearch(FoodPic)
    FoodName = FoodNames[0]
    Foodlists = ResearchFood(FoodName=FoodName)
    if len(Foodlists) == 0:
        print("未在数据库中搜索到结果！")
        exit()
    for foodlist in Foodlists:
        print(foodlist[1])
