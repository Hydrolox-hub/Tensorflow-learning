#20231210
from npython import *
import urequests

#自检查程序
#执行器与传感器
led.on()
time.sleep(1)
led.off()
rgb.write_left(255,0,0)
time.sleep(1)
rgb.write_left(0,0,0)
rgb.write_right(0,255,0)
time.sleep(1)
rgb.write_left(0,0,0)
#传感器自测程序
for i in range(5):
    oled.print(1,1,"自测试",1)
    oled.print(1,2,"温度："+str(aht20.read_temp()),1)
    oled.print(1,3,"湿度："+str(aht20.read_hum()),1)
    oled.print(1,4,"光线："+str(light.read()),1)
    oled.print(1,5,"声音："+str(sound.read()),1)
    time.sleep(1)
   
#---------
print('check-self ok!')
#程序开始执行
#(1)wifi连接网络
cip=wifi.connect("NYT_510_2.4G","88837306")
oled.fill(0)
oled.display("cip:%s" % (cip),0,0)
oled.show()
print('wifi is ok!')
#(2)设置WEB管理页面地址
IP='192.168.0.13'
PORT='5000'
url='http://%s:%s/input?' % (IP,PORT)
urlret='http://%s:%s/inputs' % (IP,PORT)
#程序执行循环
while True:
    #读取相应参数值,即环境参数
    tempval=aht20.read_temp()
    humval=aht20.read_hum()
    lightval=light.read()
    soundval=sound.read()
    #显示当前测量值
    oled.fill(0)
    oled.print(3,1,"当前环境参数",1)
    oled.print(1,2,"温度："+str(tempval),1)
    oled.print(1,3,"湿度："+str(humval),1)
    oled.print(1,4,"光线："+str(lightval),1)
    oled.print(1,5,"声音："+str(soundval),1)
    try:
        #参数上传服务器中
        data=urequests.get(url+'tempval=%d&humval=%d&lightval=%d&soundval=%d' %(tempval,humval,lightval,soundval))
        print(data.content) #s.encode("GBK")
        #从服务器中读取控制参数并进行控制
        r = urequests.get(urlret)
        print(r.content)
        #提取控制数据值
        #根据控制数据进行控制
        #controldata='0000'
        controldata=r.content #只征对于HTTP/0.9返回值，其他需处理
        print(controldata[1]-0x30==1,controldata[2]-0x30==1,controldata[3]-0x30==1,controldata[4]-0x30==1)
        #LED控制
        if controldata[1]-0x30==1:
            led.on()
        else:
            led.off()
        #RGB_LEFT控制
        if controldata[2]-0x30==1:
            rgb.write_left(255,0,0)
        else:
            rgb.write_left(0,0,0)
        #RGB_RIGHT控制
        if controldata[3]-0x30==1:
            rgb.write_right(0,255,0)
        else:
            rgb.write_right(0,0,0)
    except Exception as e:
        print("upload error!")
    #设置处理周期,即时长
    time.sleep(2)
    pass
