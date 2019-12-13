import random as rand
import tkinter as tk
import time
import math

class Flag:
    def __init__(self):
        self.__value = False
    def set_true(self, event=""):
        self.__value = True
    def set_false(self, event=""):
        self.__value = False
    def get(self):
        return self.__value

def gen_position(windowWidth, windowHeight):
    center1 = (windowWidth // 4, windowHeight // 2)
    rad = min(windowWidth // 4, windowHeight // 2)
    center2 = (center1[0] + rad * 2, center1[1])
    distX = rand.randint(-rad, rad)
    maxDistY = int(math.sqrt(rad**2 - distX**2))
    distY = rand.randint(-maxDistY, maxDistY)
    if (rand.randint(0, 1) == 0):
        center = center1
    else:
        center = center2
    x = center[0] + distX
    y = center[1] + distY
    return (x,y)

def gen_color():
    red = rand.randint(0, 4095)
    green = rand.randint(0, 4095)
    blue = rand.randint(0, 4095)
    color = '#' + '{0:03x}{1:03x}{2:03x}'.format(red, green, blue)
    return color

def main():
    pntSize = 1
    root = tk.Tk()
    root.title('Star sky')
    windowWidth = root.winfo_screenwidth()
    windowHeight = root.winfo_screenheight()
    root.attributes('-fullscreen', True)
    flag = Flag()
    flag.set_true()
    root.bind('<Key>', flag.set_false)
    canvas = tk.Canvas(root, width = windowWidth, height = windowHeight)
    canvas.pack()
    while(flag.get()):
        color = gen_color()
        (x,y) = gen_position(windowWidth, windowHeight)
        canvas.create_oval(x, y, x+pntSize, y+pntSize, outline=color, fill=color)
        root.update()
        time.sleep(0.1)
    root.destroy()
if (__name__ == '__main__'):
    main()
