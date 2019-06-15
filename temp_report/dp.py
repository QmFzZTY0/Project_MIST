#!/usr/lib/python2.7
# -*- coding:utf8 -*-

import time
import smtplib
from datetime import datetime, date, timedelta
from get_name import get_name
#import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from configparser import ConfigParser
import io



def mean(input_list):
    p_list = list(input_list)
    temp_sum = 0
    for i in range(len(p_list)):
        temp_sum += float(p_list[i][21:])
    mean = temp_sum / (len(p_list))
    return mean

config = ConfigParser()
if len(config.read('config.ini')) == 0:
    print'配置文件为空,准备创建配置文件'
    config.add_section('main')  # 添加 section
    config.set('main', 'send', 'null')
    config.set('main', 'receive', 'null')
    config.set('main','address','smtp.163.com')
    config.set('main', 'port', '25')
    config.set('main', 'send_password', 'null')
    with io.open('config.ini', 'w', encoding='utf-8') as file:
        config.write(file)
    print'配置文件创建完成,请更改配置文件后在次运行'
    exit(0)

#日期暂存
data = 0

if data != time.strftime('%d'):
    with open(get_name(-1),'r') as f:
        origin_list = f.readlines()
    mean = mean(origin_list)
    temp_max = max(origin_list)
    temp_min = min(origin_list)
    text = ('平均温度是:{:.2f}；最高温度是:{}，发生在{}；最低温度是:{}，发生在{}。'.format(mean,temp_max[21:25],temp_max[:19],temp_min[21:25],temp_min[:19]))
    print text


if config.get('main','send')=='null':
    print'配置文件未修改，停止中'
    exit(0)
else:
    fromaddr = config.get('main','send')  # 填写你的发信邮箱，我选用的是163邮箱
    toaddr = config.get('main','receive')   # 填写你的收信地址
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = '树梅派温度'   # 邮件标题
    
    body = text   # 邮件内容
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(config.get('main','address'), int(config.get('main','port')))   # 填写163邮箱的发信服务器地址
    server.starttls()
    server.login(fromaddr, config.get('main','send_password'))   # xxx代表你的邮件登录密码
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text) # 开始发邮件
    print u"send ok"  # 发送成功提示
    server.quit()