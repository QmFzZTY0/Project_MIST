#!/usr/local/python3.7
#-*- coding: utf-8 -*-  

import time
from datetime import datetime, date, timedelta
from get_name import get_name

def mean(input_list):
    p_list = list(input_list)
    temp_sum = 0
    for i in range(len(p_list)):
        temp_sum += float(p_list[i][21:])
    mean = temp_sum / (len(p_list))
    return mean


data = 0

if data != time.strftime('%d'):
    with open(get_name(-1),'r') as f:
        origin_list = f.readlines()
    mean = mean(origin_list)
    temp_max = max(origin_list)
    temp_min = min(origin_list)
    text = ('平均温度是:{:.2f}.最高温度是:{},发生在{}.最低温度是:{},发生在{}.'.format(mean,temp_max[21:25],temp_max[:19],temp_min[21:25],temp_min[:19]))
    print(text)
