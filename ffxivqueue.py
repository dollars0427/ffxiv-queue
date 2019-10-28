import pyscreenshot as ImageGrab
import time
import tkinter as tk

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
    im.show()
