import random as rand
import tkinter as tk
import time

class Flag:
    __value = False
    def set_true(self, event=""):
        self.__value = True
    def set_false(self, event=""):
        self.__value = False
    def get(self):
        return self.__value

def main():
    windowWidth = 800
    windowHeight = 240
    root = tk.Tk()
    root.title('Star sky')
    flag = Flag()
    flag.set_true()
    root.bind('<Key>', flag.set_false)
    canvas = tk.Canvas(root, width = windowWidth, height = windowHeight)
    canvas.pack()
    while(flag.get()):
        red = rand.randint(0, 4095)
        green = rand.randint(0, 4095)
        blue = rand.randint(0, 4095)
        color = '#' + '{0:03x}{1:03x}{2:03x}'.format(red, green, blue)
        x = rand.randint(0, windowWidth)
        y = rand.randint(0, windowHeight)
        canvas.create_oval(x, y, x+1, y+1, outline=color, fill=color)
        root.update()
        time.sleep(0.1)
    root.destroy()
