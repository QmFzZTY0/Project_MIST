#!/usr/local/python3.7
# -*- coding:utf8 -*-

from datetime import datetime, date, timedelta

def get_name(inf = 0):
    day = (date.today() + timedelta(days = inf)).strftime("%Y-%m-%d")
    name = '/home/pi/code/temp_report/log/'+day+'.log'
    return name
