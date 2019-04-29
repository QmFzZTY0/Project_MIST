#-*- coding: utf-8 -*-  
#this is a module for temp Monitor program

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
