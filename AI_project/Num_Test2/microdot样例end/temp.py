#网页响应程序------
#接收来自网页的按钮操作
@app.get('/ledon')
def index2(request):
    global ledflag
    ledflag=1
    return "1"
@app.get('/ledoff')
def index2(request):
    global ledflag
    ledflag=0
    return "0"
@app.get('/rgbon')
def index3(request):
    global rgbflag1
    rgbflag1=1
    return "3"
@app.get('/rgboff')
def index3(request):
    global rgbflag1
    rgbflag1=0
    return "2"
@app.get('/musicon')
def index4(request):
    global rgbflag2
    rgbflag2=1
    return "5"
@app.get('/musicoff')
def index4(request):
    global rgbflag2
    rgbflag2=0
    return "4"