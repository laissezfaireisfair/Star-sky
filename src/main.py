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
        red = rand.randint(0, 255)
        green = rand.randint(0, 255)
        blue = rand.randint(0, 255)
        color = '#' + '{0:x}{0:x}{0:x}'.format(red, green, blue)
        x = rand.randint(0, windowWidth)
        y = rand.randint(0, windowHeight)
        canvas.create_oval(x, y, x+1, +1, outline=color, fill=color)
        root.update()
