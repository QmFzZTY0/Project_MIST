import requests

try:
    f = open('cookie.txt','r')

except IOError:
    print('file 404')

else:
    for line in f.readlines():
        cookie = line.strip('\n')
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Referer':'https://steamcn.com/member.php?mod=logging&action=login',
            'Cookie':cookie
        }

    res=requests.get("https://steamcn.com/",headers=headers)

finally:
    f.close()

