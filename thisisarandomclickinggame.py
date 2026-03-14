import math
import pgzrun
import random
import time

WIDTH = 1000
HEIGHT = 800
elapsed = 0
game = True
score = 0
start = time.time()
end = 30
gs = ""

click1 = Actor("pinkdog")
click1.x = 400
click1.y = 350

def on_mouse_down(pos):
    global score
    global gs
    if click1.collidepoint(pos):


        click1.x = random.randint(10, 200)
        click1.y = random.randint(10, 200)


        click1.image = random.choice(["pinkdog", "bluhelmet"])

        score += 1
        gs = "good shot"
    else:
        gs = "bad shot"

def update():
    global elapsed, start, end, game
    elapsed = time.time() - start
    elapsed = round(elapsed, 1)
    if elapsed > end:
        game = False

def draw():
    screen.fill("white")
    click1.draw()
    screen.draw.text(f"score:{score}", (70, 50), color="black")
    screen.draw.text(gs, (70, 70), color="black")
    screen.draw.text(f"time left:{elapsed}", (70, 90), color="black")
    if game == False:
        screen.fill("white")
        screen.draw.text(f"final score:{score}", (500, 400), color="black")

pgzrun.go()
