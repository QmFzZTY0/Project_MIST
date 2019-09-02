#!/usr/local/python3.7
# -*- coding:utf8 -*-

import requests
import os

l = [] #提前创建空列表存放内容

website = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt'
traget = '/home/pi/.config/aria2/aria2.config'

def get_best(website):#获取数据并且进行处理
    res = requests.get(website)
    res = (res.text.replace('\n\n',',')).strip(',')
    return res
with open(traget,'r')as f:#读取config
        for i in f:
            if 'bt-tracker=' not in i:
                l.append(i)
            elif 'bt-tracker=' in i:
                l.append('bt-tracker={}'.format(get_best(website)))
#print (l)
with open(traget,'w')as f:#修改config
    for i in l:
        f.write(i)

os.system('sudo bash /home/pi/code/trackers_best_ip/reboot.sh')#让aria2重启

print ('ok')
