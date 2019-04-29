def config(inf):
    send = ''#发送邮箱
    receive =''#接收邮箱
    address ='smtp.163.com'#邮件服务器地址
    port ='25'#端口
    send_password =''#发送邮箱密码
    ip_txt = '/home/pi/code/sendmail/ip.txt'#ip.txt存放路径

    if inf == 'send':
        return send
    elif inf == 'receive':
        return receive
    elif inf == 'address':
        return address
    elif inf == 'port':
        return port
    elif inf == 'send_password':
        return send_password
    elif inf == 'ip_txt':
        return ip_txt
