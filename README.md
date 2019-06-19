# 为树莓派编写的一些小工具

## 目录
* [sendmail（邮件发送）](#sendmail)
* [temp_report（温度监控）](#temp_report)
* [check_in（签到）](#check_in)
* [trackers_best_ip（bt服务器选择）](#trackers_best_ip)
### sendmail
获取ip地址并用邮件发出，如果多次获取到一样ip地址则不发送，需要配置`ip.txt`路径，配置文件会在第一次运行后生成。

- [ ] 添加备选网址
- [ ] 当网址无法访问时自动切换

### temp_report
获取树莓派CPU温度并记录，配置文件会在第一次运行后生成
- [x] 自动删除多余文件
- [x] 自动分析温度信息
- [x] 自动发送温度信息

目前已知的bug：由于对比采用的字典格式是`{温度:时间}`，所以当有同样的温度出现时，只会显示最晚出现的。

### check_in
获得论坛访问奖励(失效)，配置文件会在第一次运行后生成。
- [ ] 修好它

### trackers_best_ip
获取[速度最快的BT服务器](https://github.com/ngosang/trackerslist)去除回车并加入`,`。
需要更改aria配置文件位置，且`bt-tracker`项目在文件的最后
- [x] 自动填写aria配置文件
