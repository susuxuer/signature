# -*- coding:utf-8 -*-

from Tkinter import *  # python 3 是tkinter
import tkMessageBox
import requests
import re
from PIL import Image


def download():
    start_url = 'http://www.uustv.com/'             #获取网页
    #start_url = 'http: // www.yishuzi.com /'
    name = entry.get().encode('utf-8')              #发送请求
    if not name:
        tkMessageBox.showinfo('Warning', 'Please input again！')
        return
    data = {
        'word': name,
        'sizes': '60',
        'fonts': 'jfcs.ttf',
        'fontcolor': '#000000'
    }
    result = requests.post(start_url, data=data).content
    reg = '<div class="tu">﻿<img src="(.*?)"/></div>'
    img_url = start_url + re.findall(reg, result)[0]
    response = requests.get(img_url).content
    # 将生成的签名图片下载到本地
    with open('{}.gif'.format(name.decode('utf-8').encode('gbk')), 'wb') as f:
        f.write(response)
    try:
        im = Image.open('{}.gif'.format(name.decode('utf-8').encode('gbk')))
        im.show()
    except:
        print 'open the picture'


root = Tk()
root.title('suxue_version')
root.geometry('+800+500')  # 设置窗口出现在屏幕上面的位置
Label(root, text='Name:', font=('微软雅黑', 15)).grid()  # 布局方法不要混用
entry = Entry(root, font=('微软雅黑', 15))
entry.grid(row=0, column=1)
button = Button(root, text='Design your name', font=('微软雅黑', 15), width='15', height=1, command=download)
button.grid(row=1, column=1)
root.mainloop()
