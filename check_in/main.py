#!/usr/local/python3.7
# -*- coding:utf8 -*-
#check_in

import requests
from configparser import ConfigParser


config = ConfigParser()
#print(len(config.read('config.ini'))==0)
if len(config.read('config.ini')) == 0:
    print('配置文件为空,准备创建配置文件')
    config.add_section('bbs1')
    config.set('bbs1','cookie','null')
    config.set('bbs1', 'target', 'null')
    with open('config.ini', 'w', encoding='utf-8') as file:
        config.write(file)
    print('配置文件创建完成,请更改配置文件后在次运行')
    exit(0)
config.read('config.ini')
for i in config.sections():
    cookie=config.get(i,'cookie')
    if cookie=='null':
        print('配置文件未填写，自动退出')
        exit(0)
    print(cookie)
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Cookie':cookie
    }
#    print (i)
    res=requests.get(config.get(i,'target'),headers=headers)
