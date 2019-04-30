import requests
from config import config

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Referer':config('referer'),
        'Cookie':config('cookie')
        }

res=requests.get(config('target'),headers=headers)
