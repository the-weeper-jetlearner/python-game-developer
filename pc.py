import random
import pgzrun
import time

WIDTH = 1000
HEIGHT = 1000
gamestate = 1

def update():
    pass
def lv1():

    global gamestate
    if gamestate == 1:
        gamestate = 2
def lv2():
    global gamestate   
    if gamestate == 2:   
       gamestate = 3
def lv3():
    global gamestate
    if gamestate == 3:
        gamestate = 4
def lv4():
    if gamestate == 4:
        pass

def draw():
    global gamestate
    screen.blit("pc",(0,0))
    if gamestate == 1:
        screen.draw.text("this is a game about a dude at a pc",(500, 200))
    if gamestate == 2:
        screen.draw.text("this is a game about a dude at a pc",(500, 200))
        screen.draw.text("\n He got trapped in a pc",(500, 300))
    if gamestate == 3:
        screen.draw.text("this is a game about a dude at a pc",(500, 200))
        screen.draw.text("\n He got trapped in a pc",(500, 300))
        screen.draw.text("\n your task: Get him out of there",(500, 400))
    if gamestate == 4:
        screen.draw.text("this is a game about a dude at a pc",(500, 200))
        screen.draw.text("\n He got trapped in a pc",(500, 300))
        screen.draw.text("\n your task: Get him out of there",(500, 400))
        screen.draw.text("\n Using logic...",(500, 500))
clock.schedule(lv1,1)
clock.schedule(lv2,2)
clock.schedule(lv3,3)
clock.schedule(lv4,4)
pgzrun.go()
