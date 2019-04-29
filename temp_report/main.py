#!/usr/local/opt/python-3.7.0/lib/python3.7
# -*- coding: utf-8 -*-  

import time
import os
from get_temp import get_temp
from get_name import get_name

date = 0

def p_name():
	result = time.strftime('%Y-%m-%d %X')+'\t'+get_temp()+'\n'
	return result

if date != time.strftime('%d'):
	open(get_name(), 'a').close()
	date = time.strftime('%d')
with open(get_name(), 'a') as f:
	f.write(p_name())

