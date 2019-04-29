#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import urllib
import urllib2
from config import config


user_agent = 'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT)'
headers = {}
headers['User-Agent'] = user_agent
url = 'http://members.3322.org/dyndns/getip'   # 通过这个接口获取公网IP地址
req = urllib2.Request(url, headers = headers)
res = urllib2.urlopen(req)

ip = string.strip(res.read())   # 去除空格
print ip

while True:
    try:
        f=open(config('ip_txt'),'r')
        break
    except:
        f=open(config('ip_txt'),'w')
if f.read()==ip:
    print 'pass'
    f.close()
else:
    fromaddr = config('send')  # 填写你的发信邮箱，我选用的是163邮箱
    toaddr = config('receive')   # 填写你的收信地址，接收树莓派的公网IP地址
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'rasperberry IP is ' + ip   # 邮件标题
    
    body = 'rasperberry IP is ' + ip   # 邮件内容，同标题（偷懒）
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(config('address'), config('port'))   # 填写163邮箱的发信服务器地址
    server.starttls()
    server.login(fromaddr, config('send_password'))   # xxx代表你的邮件登录密码
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text) # 开始发邮件
    print u"send ok"  # 发送成功提示
    server.quit()
    f.close()
    with open(config('ip_txt'),'w') as f:
        f.write(ip)
