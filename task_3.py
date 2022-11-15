from turtle import *
from random import randint


def mountains(step):
    speed("fast")
    forward(600)
    goto(-600, 0)
    forward(50)
    mountain = [50, 100, 150, 155, 160, 320, 330, 340, 400, 380, 360, 200, 150, 120, 130, 100, 50, 20]
    for i in range(len(mountain)):
        goto(i * step, mountain[i] + randint(-10, 10))


for i in range(randint(1, 5)):
    mountains(randint(20, 40))
exitonclick()
