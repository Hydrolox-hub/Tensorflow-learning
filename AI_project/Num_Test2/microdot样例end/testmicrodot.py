from npython import wifi,led,rgb,oled,light,time,sound,aht20
# 导入Microdot
from microdot import Microdot,Response
from temphtml import htmltemp1
import uio
# 使用uio.StringIO类创建一个文本流对象
#s = uio.StringIO(text)

# 网络连接参数
ipserver="NYT_510_2.4G" #热点名称
ippass="88837306" #热点密码
#ipserver="HONOR30S" #热点名称
#ippass="12345678" #热点密码
#网络连接
ip=wifi.connect(ipserver,ippass)
oled.print(1,1,ip,1)
time.sleep(2)

# 实例化这个类
app = Microdot()
#----------------
#----------------
htmltemp2="</body></html>"
showmode=""
msg=Response()
msg.body=uio.StringIO(showmode)
msg.headers['Content-Type'] = 'text/html; charset=UTF-8'

@app.route('/')
def index1(request):
    showmode=htmltemp1+"<h1>光线：%s,声音：%s</h1><br><h1>温度：%s,湿度：%s</h1>" % (light.read(),sound.read(),aht20.read_temp(),aht20.read_hum())+htmltemp2
    msg.body=uio.StringIO(showmode)
    return msg


@app.get('/ledon')
def index2(request):
    # 如果收到get请求on就开灯
    led.on()
    return "开灯了"

@app.get('/ledoff')
def index2(request):
    # 如果收到get请求off就关灯
    led.off()
    return "关灯了"

@app.get('/rgbon')
def index3(request):
    rgb.write_left(255,0,0)
    return "红色灯了"

@app.get('/rgboff')
def index3(request):
    rgb.write_left(0,0,0)
    return "红灯灭了"

@app.get('/musicon')
def index4(request):
    #music.play(gequ[2])
    #time.sleep(1)
    rgb.write_right(0,255,0)
    return "音乐响了"

@app.get('/musicoff')
def index4(request):
    #music.stop()
    rgb.write_right(0,0,0)
    return "音乐停了"

while True:
    try:
        app.run()
        print("get a right done!")
    except Exception as e:
        #print(e)
        pass

#端口5000
#app.run(host='0.0.0.0', port=5000, debug=False, ssl=None)