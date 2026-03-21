import pgzrun
import random
WIDTH = 1200
HEIGHT = 1000
char = Actor("bee")
char.x = 100
char.y = 100
flag = False
rat = Actor("rat")
rat.x = random.randint(300,600)
game = True
rat.y= random.randint(300,600)
def draw ():
    screen.blit("background",(0,0))
    char.draw()
    rat.draw()
    if game == False:
        screen.fill("black")
def move_rat():
    global flag
    flag = True
    
def update():
    global game
    if keyboard.left:
        char.x += -10
    if keyboard.right:
        char.x += 10
    if keyboard.down:
        char.y += 10
    if keyboard.up:
        char.y += -10
    if flag == True:
        if rat.x < char.x:
            rat.x += 5
        if rat.x > char.x:
            rat.x -= 5
        if rat.y > char.y:
            rat.y -= 5
        if rat.y < char.y:
            rat.y += 5
        if char.colliderect(rat):
            game = False 
clock.schedule(move_rat,5)
pgzrun.go()
