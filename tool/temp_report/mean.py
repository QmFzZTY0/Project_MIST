#-*- coding: utf-8 -*-  
#this is a module for temp Monitor program

def mean(input_list):
	p_list = list(input_list)
	temp_sum = 0
	for i in range(len(p_list)):
		temp_sum += float(p_list[i][21:])
	mean = temp_sum / (len(p_list))
	return mean
