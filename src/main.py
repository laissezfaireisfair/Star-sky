import random as rand
import tkinter as tk

def main():
    windowWidth = 800
    windowHeight = 240
    root = tk.Tk()
    root.title = 'Star sky'
    canvas = tk.Canvas(root, width = windowWidth, height = windowHeight)
    canvas.pack()
    continueDraw = True
    while(continueDraw):
        red = rand.randint(0, 4095)
        green = rand.randint(0, 4095)
        blue = rand.randint(0, 4095)
        color = '#' + '{0:03x}{1:03x}{2:03x}'.format(red, green, blue)
        x = rand.randint(0, windowWidth)
        y = rand.randint(0, windowHeight)
        canvas.create_oval(x, y, x+1, y+1, outline=color, fill=color)
        root.update()
