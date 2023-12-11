# -*- coding: utf_8 -*-
# [Python/Mybit]
from npython import *           # 导入npython模块
#回调函数
def event(topic,msg):
	data=str(msg.decode('uft-8'))
	oled.print(1,4,data,1)
	data1=eval(data) #转成词典
	print(topic,data1)
	if data1["msg"] == "LEDON":
		led.on()
	if data1["msg"] == "LEDOFF":
		led.off()

IP=wifi.connect("NYT_510_2.4G","88837306")
oled.print(1,1,str(IP),1)
mqtt.config("121.5.75.157",1883)
mqtt.connect()
oled.print(1,2,"MQTT连接成功",1)
mqtt.subscribe("Weather/sensor",event)
while True:
	mqtt.publish("Weather/sensor","LEDON")
	time.sleep(1)
	mqtt.check_msg()
	time.sleep(2)
	mqtt.publish("Weather/sensor","LEDOFF")
	time.sleep(1)
	mqtt.check_msg()
	time.sleep(2)