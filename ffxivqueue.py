import pyscreenshot as ImageGrab
import time
import json
import requests
import tkinter as tk
import os
from threading import Timer
from tkinter import ttk

with open('setting.json', 'r') as setting_file:
    setting = json.load(setting_file)

#取得屏幕大小
win = tk.Tk()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

#取得排队视窗位置
x1 = screen_width / 2 - 60
y1 = screen_height / 2 - 20
x2 = x1 + 40
y2 = y1 + 30

first_run = True
should_stop = False

def before_screenshot():
    qq_number_label.pack_forget()
    qq_nubmer.pack_forget()
    repeat_time_label.pack_forget()
    repeat_time.pack_forget()
    start_button.place_forget()
    stop_button.place(x=210, y=230)
    info_label.pack()

    repeat_time_min = int(repeat_time_value.get())
    repeat_time_second = repeat_time_min * 60
    t = Timer(repeat_time_second, screenshot)
    t.start()

#停止Screenshot動作
def stop_screenshot():
    global should_stop
    should_stop = True
    title_label.pack()
    qq_number_label.pack()
    qq_nubmer.pack()
    repeat_time_label.pack()
    repeat_time.pack()
    stop_button.place_forget()
    start_button.place(x=210, y=230)

def screenshot():
    #取得用戶輸入的通知用QQ號，並將之寫入儲存檔
    qq = qq_number_value.get()
    with open('save_data.json', 'w') as save_file:
        save_data = {'qq_number': qq}
        json.dump(save_data, save_file)
    repeat_time_min = int(repeat_time_value.get())
    repeat_time_second = repeat_time_min * 60
    #在接收停止訊號前，不斷重覆抓取動作並發送至API
    global should_stop
    if should_stop != True:
        im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        im.save('queuenum.png')
        with open('queuenum.png', 'rb') as f:
            data = {'qq': qq}
            r = requests.post(setting['api_url'], data=data, files={'queuenum.png': f})
            print(r.text)
            time.sleep(repeat_time_second)
            screenshot()
    else:
        print('Stopped!')
        first_run = True
        should_stop = False
#建构介面
win.title('FF14 排队检测器')
win.geometry('500x300')

#标题
title_label = tk.Label(win, text='欢迎使用FF14排队检测器', font=('Arial', 30), width=30, height=2)
title_label.pack()

#QQ号码
qq_number_label = tk.Label(win, text='接收通知的QQ号码:', font=('Arial', 15), width=30, height=2)
qq_number_label.pack()

#若用戶存檔已建立，從存檔裡讀取通知用QQ號
if os.path.isfile('save_data.json'):
    with open('save_data.json', 'r') as save_file:
        save = json.load(save_file)
        saved_qq_number = save['qq_number']
        qq_number_value = tk.StringVar(value=saved_qq_number)
else:
    qq_number_value = tk.StringVar()

qq_nubmer = tk.Entry(win, show=None, font=('Arial', 14), textvariable=qq_number_value)
qq_nubmer.pack()

#通知频率
repeat_time_label = tk.Label(win, text='通知频率（分钟）:', font=('Arial', 15), width=30, height=2)
repeat_time_label.pack()
repeat_time_value = tk.StringVar()
repeat_time_value.set("10")
repeat_time = tk.Entry(win, show=None, font=('Arial', 14), textvariable=repeat_time_value)
repeat_time.pack()

#开始按钮
start_button = ttk.Button(win, text='开始', command=before_screenshot)
start_button.place(x=210, y=230)

info_label = tk.Label(win, text='侦测器已运行，请切换至游戏画面。', font=('Arial', 15), width=30, height=2)
#停止按钮
stop_button = ttk.Button(win, text='停止', command=stop_screenshot)
win.mainloop()
