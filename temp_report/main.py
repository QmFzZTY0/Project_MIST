#!/usr/local/opt/python-3.7.0/lib/python3.7
# -*- coding: utf-8 -*-  

import time
import os

date = 0

def get_name():
	name = '/home/pi/code/temp_report/log/'+time.strftime('%Y-%m-%d')+'.log'
	return name

def get_temp():
	file = open("/sys/class/thermal/thermal_zone0/temp")   
	temp = float(file.read()) / 1000  
	file.close()  
	t = ("temp : %.1f" %temp)[6:] 
	return t


def p_name():
	result = time.strftime('%Y-%m-%d %X')+'\t'+get_temp()+'\n'
	return result

if date != time.strftime('%d'):
	open(get_name(), 'a').close()
	date = time.strftime('%d')
with open(get_name(), 'a') as f:
	f.write(p_name())

