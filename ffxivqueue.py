import pyscreenshot as ImageGrab
import time
import tkinter as tk
import requests

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x1 = screen_width / 2 - 60
y1 = screen_height / 2 - 20
x2 = x1 + 40
y2 = y1 + 30

if __name__ == '__main__':
    time.sleep(5)
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im.save('queuenum.png')
    im.show()
    with open('queuenum.png', 'rb') as f:
        data = {'qq': 2590519016}
        r = requests.post('http://127.0.0.1:1000', data=data, files={'queuenum.png': f})
        print(r.text)
