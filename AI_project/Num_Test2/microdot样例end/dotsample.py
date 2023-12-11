from npython import wifi,oled,time
# 导入Microdot
from microdot import Microdot,Response
import uio
# 使用uio.StringIO类创建一个文本流对象
#s = uio.StringIO(text)
global ledflag,rgbflag1,rgbflag2,data1,data2,data3,data4,musicflag
ledflag=0;rgbflag1=0;rgbflag2=0;musicflag=0
data1=0;data2=0;data3=0;data4=0
# 网络连接参数
ipserver="NYT_510_2.4G" #热点名称
ippass="88837306" #热点密码
#网络连接
ip=wifi.connect(ipserver,ippass)
oled.print(1,1,ip,1)
time.sleep(2)

# 实例化这个类
app = Microdot()
#----------------
from temphtml import htmltemp1
htmltemp2="</body></html>"
showmode=""
msg=Response()
msg.body=uio.StringIO(showmode)
msg.headers['Content-Type'] = 'text/html; charset=UTF-8'

@app.route('/')
def index1(request):
    global data1,data2,data3,data4
    showmode=htmltemp1+"<h1>温度：%s,湿度：%s</h1><br><h1>光线：%s,声音：%s</h1>" % (data1,data2,data3,data4)+htmltemp2
    msg.body=uio.StringIO(showmode)
    return msg
while True:
    try:
        app.run()
        print("get a right done!")
    except Exception as e:
        #print(e)
        pass

#端口5000
#app.run(host='0.0.0.0', port=5000, debug=False, ssl=None)