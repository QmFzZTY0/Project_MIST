#!/usr/local/opt/python-3.7.0/lib/python3.7
#-*- coding: utf-8 -*-  

import time
from datetime import datetime, date, timedelta


yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")

def get_name():
	name = '/home/pi/code/temp_report/log/'+yesterday+'.log'
	return name
	
def median(input_list):
        p_list = list(input_list)
        p_list.sort()
        for i in range(len(p_list)):
                p_list[i] = float(p_list[i][21:])
        if len(p_list)%2 == 1:
                return p_list[int(len(p_list)//2)]
        else:
                data_list = [p_list[int(len(p_list)//2-1)],p_list[int(len(p_list)//2)]]
                return (data_list[1] + data_list[0])/2

def mean(input_list):
	p_list = list(input_list)
	temp_sum = 0
	for i in range(len(p_list)):
		temp_sum += float(p_list[i][21:])
	mean = temp_sum / (len(p_list))
	return mean




data = 0

if data != time.strftime('%d'):
	with open(get_name(),'r') as f:
		origin_list = f.readlines()
	mean = mean(origin_list)
	median = median(origin_list)
	temp_max = max(origin_list)
	temp_min = min(origin_list)
	print ('mean is',mean)
	print ('\nmedian is',median)
	print ('\nMaximum temperature is',temp_max[21:])
	print ('\thappen in',temp_max[:21])
	print ('\nMinimum temperature is',temp_min[21:])
	print ('\thappen in',temp_min[:21])
