import pgzrun
import random
WIDTH = 1200
HEIGHT = 1000
players = ["purple","greem","red","orange"]
centrex = WIDTH /2
centrey = HEIGHT /2
center = (centrex , centrey)
level = 1
finallevel = 5
gamecomplete = False
gameover = False
items = []
animations =[]

def update():
    global items
    if len(items) == 0:
        makeplayer()
def makeplayer():
    player = Actor("blue")
    items.append(player)
    for i in range(level):
        img = random.choice(players)
        player = Actor(img)
        items.append(player)

def draw():
    screen.fill("white")
    if gamecomplete == True:
        screen.fill("green")
        screen.draw.text("you won",center)
    elif gameover == True:
        screen.fill("red")
        screen.draw.text("you lost, scram",center)
    else:
        for item in items:
            item.draw()
pgzrun.go()
