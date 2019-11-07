import turtle
import random

turtle.bgcolor("black")
gordon = turtle.Turtle()
gordon.shape("circle")

gordon.speed(0)

colors = ("dimgray", "darkviolet", "gray", "indigo", "darkgray", "darkmagenta")

for i in range(360):
    gordon.color(colors[i % 6])
    gordon.circle(i*1)
    gordon.left(5)

turtle.done()