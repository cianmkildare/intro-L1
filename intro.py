import pgzrun 

from random import randint

WIDTH = 400
HEIGHT = 400
TITLE = "introduction"

def draw():
    width = 400
    height = 100

    for i in range (30):
        r = 100
        g = randint(0,255)
        b = randint(0,255)

        rect = Rect((0,0),(width,height))
        rect.center = 200,200

        screen.draw.rect(rect,(r,g,b))

        width = width - 10
        height = height + 10











pgzrun.go()

