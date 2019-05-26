import requests


def get_best(website,file_name):
	res = requests.get(website)
	res = res.text.replace('\n\n',',')
	with open(file_name,'w') as f:
		f.write(res)
get_best('https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best_ip.txt','best_ip.txt')
get_best('https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt','best_website.txt')
