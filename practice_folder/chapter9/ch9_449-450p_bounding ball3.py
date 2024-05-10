from tkinter import *
import time
import random

window = Tk()
canvas = Canvas(window, width = 600, height = 400)
canvas.pack()
class Ball():
    def __init__(self, color, size):
        self.id = canvas.create_oval(0,0,size, size, fill = color)
        self.dx = random.randint(1,10)
        self.dy = random.randint(1,10)
    
    def move(self):
        canvas.move(self.id, self.dx, self.dy)
        x0, y0, x1, y1 = canvas.coords(self.id)
        if y1 > canvas.winfo_height() or y0 < 0:
            self.dy = -self.dy
        if x1 > canvas.winfo_height() or x0 < 0:
            self.dx = -self.dx

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
ballList = []
for i in range(30):
    ballList.append(Ball(random.choice(colors), 60))

while True:
    for i in range(30):
        ballList[i].move()
    window.update()
    time.sleep(0.05)
window.mainloop()
