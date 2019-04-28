#!/usr/local/opt/python-3.7.0/lib/python3.7
#-*- coding: utf-8 -*-  

import time
from datetime import datetime, date, timedelta
from mean import mean
from median import median


yesterday = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")

def get_name():
	name = '/home/pi/code/temp_control/log/'+yesterday+'.log'
	return name
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
