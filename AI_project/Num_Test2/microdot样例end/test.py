from npython import *
from machine import RTC
#建一个时钟对像
rtc = RTC()
#或时间初值进行设定，而不从网络中设置
rtc.datetime((2023, 11, 14, 1,15, 59, 40, 0)) # （年，月，日，星期，时，分，秒，子秒)
print("当前时间：", rtc.datetime())
#从网络中进行时钟校正
# 网络连接参数
ipserver="NYT_510_2.4G" #热点名称
ippass="88837306" #热点密码
#网络连接
ip=wifi.connect(ipserver,ippass)
# 校正系统主板时钟
import ntptime
ntptime.host = "cn.ntp.org.cn"#'ntp2.aliyun.com'
ntptime.settime() # set the rtc datetime from the remote server
rtc.datetime()    # get the date and time in UTC
print("当前时间：", rtc.datetime())
