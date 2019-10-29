import pyscreenshot as ImageGrab
import time
import tkinter as tk
import requests

win = tk.Tk()
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x1 = screen_width / 2 - 60
y1 = screen_height / 2 - 20
x2 = x1 + 40
y2 = y1 + 30

win.title('FF14 排队检测器')
button=tk.Button(win, text='OK')
button.pack() #顯示元件
win.mainloop()

"""
if __name__ == '__main__':
    time.sleep(5)
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im.save('queuenum.png')
    im.show()
    with open('queuenum.png', 'rb') as f:
        data = {'qq': 2590519016}
        r = requests.post('http://127.0.0.1:1000', data=data, files={'queuenum.png': f})
        print(r.text)
"""
