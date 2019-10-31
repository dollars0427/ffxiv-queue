import pyscreenshot as ImageGrab
import time
import requests
import tkinter as tk
from tkinter import ttk

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
def screenshot():
    qq = qq_number_value.get()
    repeat_time_second = repeat_time.get() * 60
    if __name__ == '__main__':
        global first_run
        if first_run == True:
            time.sleep(5)
            first_run = False
        im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        im.save('queuenum.png')
        im.show()
        with open('queuenum.png', 'rb') as f:
            data = {'qq': qq}
            r = requests.post('http://127.0.0.1:1000', data=data, files={'queuenum.png': f})
            print(r.text)
        time.sleep(repeat_time_second)
#建构介面
win.title('FF14 排队检测器')
win.geometry('500x300')

#标题
title_label = tk.Label(win, text='欢迎使用FF14排队检测器', font=('Arial', 30), width=30, height=2)
title_label.pack()

#QQ号码
qq_number_label = tk.Label(win, text='接收通知的QQ号码:', font=('Arial', 15), width=30, height=2)
qq_number_label.pack()
qq_number_value = tk.StringVar()
qq_nubmer = tk.Entry(win, show=None, font=('Arial', 14), textvariable=qq_number_value)
qq_nubmer.pack()

#通知频率
repeat_time_label = tk.Label(win, text='通知频率（分钟）:', font=('Arial', 15), width=30, height=2)
repeat_time_label.pack()
repeat_time_value = tk.StringVar()
repeat_time_value.set("30")
repeat_time = tk.Entry(win, show=None, font=('Arial', 14), textvariable=repeat_time_value)
repeat_time.pack()

start_button = ttk.Button(win, text='开始', command=screenshot)
start_button.place(x=210, y=230)
win.mainloop()
