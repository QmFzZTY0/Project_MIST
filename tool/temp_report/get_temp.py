#-*- coding: utf-8 -*-
#this is a module for temp Monitor program

def get_temp():
	file = open("/sys/class/thermal/thermal_zone0/temp")   
	temp = float(file.read()) / 1000  
	file.close()  
	t = ("temp : %.1f" %temp)[6:] 
	return t
