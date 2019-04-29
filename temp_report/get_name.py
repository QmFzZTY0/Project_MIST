#-*- coding: utf-8 -*-
#this is a module for temp Monitor program
import time
def get_name():
	name = '/home/pi/code/temp_report/log/'+time.strftime('%Y-%m-%d')+'.log'
	return name
