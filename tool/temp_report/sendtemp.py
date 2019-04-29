#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import string
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


fromaddr = "sendmaill_Delta@163.com"  # 填写你的发信邮箱，我选用的是163邮箱
toaddr = "1229278370@qq.com"   # 填写你的收信地
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'rasperberry temp '   # 邮件标题

body = 'rasperberry IP is ' +    # 邮件内容，同标题（偷懒）
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.163.com', 25)   # 填写163邮箱的发信服务器地址
server.starttls()
server.login(fromaddr, "110120119z")   # xxx代表你的邮件登录密码
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text) # 开始发邮件
print u"send ok"  # 发送成功提示
server.quit()
