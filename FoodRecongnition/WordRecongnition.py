#!  conda env
# -*- coding:utf-8 -*-
# Time:2021/2/25 下午12:02
# Author : nishizzma
# File : WordRecongnition.py


import requests
import base64
import configparser
import json


def FoodNameSearch(text):
    '''
    美食识别函数
    :param PicturePath :  等待识别图片所在位置
    :return :       图片识别结果的前5项名称
    '''
    CONFIG_PATH = '../config.ini'
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)

    NameList = []
    request_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer"

    #text = "|||||10寸蛋糕胚||||1个|||||淡奶油|||900克|||||糖粉|||10克|||"

    #对照片进行上传，选取最高可能性的5个
    params = {"text": text}
    text = json.dumps(params)
    #来源于RequestToken获得结果
    access_token = config["Word_API"]["Token"]
    request_url = request_url + "?charset=UTF-8&access_token=" + access_token
    headers = {'Content-Type': 'application/json'}
    response = requests.post(request_url, data=text, headers=headers)
    context = response.content.decode()
    words = json.loads(context)
    '''
    {'loc_details': [], 'byte_offset': 0, 'uri': '', 'pos': 'w', 'ne': '', 'item': '|', 'basic_words': ['|'], 'byte_length': 1, 'formal': ''}
    '''
    wordlist = []
    try:
        for word in words['items']:
            if word['pos'] == 'n':
                wordlist.append(word['item'])
    except:
        print("词组缺失")
    return wordlist


if __name__ == '__main__':
    text = "|||||10寸蛋糕胚||||1个|||||淡奶油|||900克|||||糖粉|||10克|||"
    FoodNameSearch(text)
