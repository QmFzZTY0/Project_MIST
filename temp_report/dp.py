#!/usr/local/python3.7
#-*- coding: utf-8 -*-  

import time
from datetime import datetime, date, timedelta
from get_name import get_name

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
	with open(get_name(-1),'r') as f:
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
