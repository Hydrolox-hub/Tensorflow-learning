htmltemp1="\
<!DOCTYPE html>\r\n\
<html lang=\"en\">\r\n\
<head>\r\n\
    <meta charset=\"UTF-8\">\r\n\
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\r\n\
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n\
    <title>esp32服务器网页</title>\r\n\
    <style>\r\n\
        * {\r\n\
            margin: 0;\r\n\
            padding: 0;\r\n\
        }\r\n\
        button {\r\n\
            width: 200px;\r\n\
            height: 50px;\r\n\
        }\r\n\
    </style>\r\n\
</head>\r\n\
<body>\r\n\
    <h1>操作控制小网页</b></h1>\r\n\
    <!--自动刷新时间设置-->\r\n\
    <meta http-equiv=\"refresh\" content=\"5\">\r\n\
    <button class=\"ledon\">LED开灯</button>\r\n\
    <button class=\"ledoff\">LED关灯</button><br><br>\r\n\
    <button class=\"rgbon\">左RGB开灯</button>\r\n\
    <button class=\"rgboff\">左RGB关灯</button><br><br>\r\n\
    <button class=\"musicon\">右RGB开灯</button>\r\n\
    <button class=\"musicoff\">右RGB关灯</button>\r\n\
    <script>\r\n\
        const ledonBtn = document.querySelector(\".ledon\");\r\n\
        const ledoffBtn = document.querySelector(\".ledoff\");\r\n\
        const rgbonBtn = document.querySelector(\".rgbon\");\r\n\
        const rgboffBtn = document.querySelector(\".rgboff\");\r\n\
        const musiconBtn = document.querySelector(\".musicon\");\r\n\
        const musicoffBtn = document.querySelector(\".musicoff\");\r\n\
        // 监听按钮点击事件\r\n\
        ledonBtn.addEventListener(\"click\", (e) => {\r\n\
            fetch(\"/ledon\", {\r\n\
                method: \"get\",\r\n\
            }).then(e => {\r\n\
                console.log(\"消息\", e);\r\n\
            }).catch(error => {\r\n\
                console.log(\"报错了\", error);\r\n\
            })\r\n\
        })\r\n\
        ledoffBtn.addEventListener(\"click\", (e) => {\r\n\
            fetch(\"/ledoff\").then(e => {\r\n\
                console.log(\"消息\", e);\r\n\
            }).catch(error => {\r\n\
                console.log(\"报错了\", error);\r\n\
            })\r\n\
        })\r\n\
        rgbonBtn.addEventListener(\"click\", (e) => {\r\n\
            fetch(\"/rgbon\", {\r\n\
                method: \"get\",\r\n\
            }).then(e => {\r\n\
                console.log(\"消息\", e);\r\n\
            }).catch(error => {\r\n\
                console.log(\"报错了\", error);\r\n\
            })\r\n\
        })\r\n\
        rgboffBtn.addEventListener(\"click\", (e) => {\r\n\
            fetch(\"/rgboff\").then(e => {\r\n\
                console.log(\"消息\", e);\r\n\
            }).catch(error => {\r\n\
                console.log(\"报错了\", error);\r\n\
            })\r\n\
        })\r\n\
        musiconBtn.addEventListener(\"click\", (e) => {\r\n\
            fetch(\"/musicon\", {\r\n\
                method: \"get\",\r\n\
            }).then(e => {\r\n\
                console.log(\"消息\", e);\r\n\
            }).catch(error => {\r\n\
                console.log(\"报错了\", error);\r\n\
            })\r\n\
        })\r\n\
        musicoffBtn.addEventListener(\"click\", (e) => {\r\n\
            fetch(\"/musicoff\").then(e => {\r\n\
                console.log(\"消息\", e);\r\n\
            }).catch(error => {\r\n\
                console.log(\"报错了\", error);\r\n\
            })\r\n\
        })\r\n\
    </script>"
print(htmltemp1)