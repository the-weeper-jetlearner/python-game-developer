import pgzrun
import random
WIDTH = 800
HEIGHT = 600
player = Actor("ship")
player.x = 300
player.y = 400
game = True
bugs=[]
bullets=[]
def spawn_bugs ():
    for _ in range(18):
        enemie = Actor("enemie")
        enemie.pos = (random.randint(50, 750), random.randint(0, 200))
        bugs.append(enemie)

def shoot ():
    global player
    global bullets
    bullet = Actor("bullet")
    bullet.pos = player.x,player.y -20
    bullets.append(bullet)


def on_key_down(key):
    if key == keys.SPACE:
        shoot()

def update():
    global player
    global game
    if keyboard.left:
        player.x += -7
    if keyboard.right:
        player.x += 7
    for bullet in bullets:
        bullet.y -= 5
    for enemie in bugs:
        enemie.y += 0.5
        if player.colliderect(enemie):
            game = False
        for bullet in bullets:
            if enemie.colliderect(bullet):
                bugs.remove(enemie)
                bullets.remove(bullet)

spawn_bugs()
def draw ():
    screen.blit("space",(0,0))
    player.draw()
    for bullet in bullets:
        bullet.draw()
    for enemie in bugs:
        enemie.draw()
    if game == False:
        screen.fill("black")

pgzrun.go()
