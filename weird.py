import pgzrun
import pygame

WIDTH = 1000
HEIGHT = 800

def draw():
    screen.fill("black")
    w = 900
    h = 200
    for i in range (25):
        r1 = Rect ((500,500),(w,h))
        r1.center = 500,400
        screen.draw.rect(r1,"blue")
        w-=28
        h+=25
def update():
    pass
pgzrun.go()