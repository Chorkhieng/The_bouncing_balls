from tkinter import *
import time
from balls import *

window = Tk()

WIDTH = 2000
HEIGHT = 1000

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="yellow")
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 25, 1, 1, "yellow")
tennis_ball = Ball(canvas, 0, 0, 10, 4, 3, "green")
basketball = Ball(canvas, 0, 0, 15, 8, 10, "black")
ball1 = Ball(canvas, 0, 0, 30, 7, 2, "black")
ball2 = Ball(canvas, 0, 0, 35, 3, 9, "red")
ball3 = Ball(canvas, 0, 0, 40, 2, 6, "purple")
ball4= Ball(canvas, 0, 0, 50, 9, 1, "cyan")
ball5 = Ball(canvas, 0, 0, 20, 7, 2, "blue")
ball6 = Ball(canvas, 0, 0, 30, 7, 5, "aqua")
ball7 = Ball(canvas, 0, 0, 30, 9, 2, "alice blue")
ball8 = Ball(canvas, 0, 0, 60, 7, 10, "cyan")
ball9 = Ball(canvas, 0, 0, 10, 1, 2, "grey")
ball10 = Ball(canvas, 0, 0, 30, 5, 2, "pink")
ball11 = Ball(canvas, 0, 0, 70, 8, 2, "black")
ball12 = Ball(canvas, 0, 0, 50, 10, 2, "grey")
ball13 = Ball(canvas, 0, 0, 15, 9, 10, "green")
ball14 = Ball(canvas, 0, 0, 20, 12, 2, "blue")
ball15 = Ball(canvas, 0, 0, 40, 7, 12, "pink")
ball16 = Ball(canvas, 0, 0, 30, 8, 2, "red")
ball17 = Ball(canvas, 0, 0, 20, 7, 8, "grey")
ball18 = Ball(canvas, 0, 0, 35, 8, 2, "red")

while True:
    volley_ball.move()
    tennis_ball.move()
    basketball.move()
    ball1.move()
    ball2.move()
    ball3.move()
    ball4.move()
    ball5.move()
    ball6.move()
    ball7.move()
    ball8.move()
    ball9.move()
    ball10.move()
    ball11.move()
    ball12.move()
    ball13.move()
    ball14.move()
    ball15.move()
    ball16.move()
    ball17.move()
    ball18.move()
    window.update()
    time.sleep(0.01)

window.mainloop()