import pgzrun
import random

WIDTH = 800
HEIGHT = 600

player = Actor("ship")
player.pos = (400, 500)

game = True
level = 1

bugs = []
bullets = []

spaceshooters = []
enemy_bullets = []



def spawn_bugs():
    for _ in range(18):
        enemie = Actor("enemie")
        enemie.pos = (random.randint(50, 750), random.randint(0, 200))
        bugs.append(enemie)



def spawn_spaceshooters():
    for _ in range(2):
        shooter = Actor("spaceshoot-removebg-preview")
        shooter.pos = (random.randint(200, 600), 80)

        shooter.hp = 30  
        spaceshooters.append(shooter)



def shoot():
    bullet = Actor("bullet")
    bullet.pos = (player.x, player.y - 20)
    bullets.append(bullet)
    sounds.thing.play()



def enemy_shoot(shooter):
    bullet = Actor("bullet")
    bullet.pos = (shooter.x, shooter.y + 20)
    enemy_bullets.append(bullet)


def on_key_down(key):
    if key == keys.SPACE:
        shoot()


def update():
    global game, level

    if not game:
        return

    if keyboard.left:
        player.x -= 7
    if keyboard.right:
        player.x += 7

    for bullet in bullets[:]:
        bullet.y -= 5
        if bullet.y < 0:
            bullets.remove(bullet)

    if level == 1:
        for enemie in bugs[:]:
            enemie.y += 0.5

            if player.colliderect(enemie):
                game = False

            for bullet in bullets[:]:
                if enemie.colliderect(bullet):
                    if enemie in bugs:
                        bugs.remove(enemie)
                    if bullet in bullets:
                        bullets.remove(bullet)

        if len(bugs) == 0:
            level = 2
            spawn_spaceshooters()


    elif level == 2:
        for shooter in spaceshooters[:]:


            if player.x < shooter.x:
                shooter.x -= 2
            elif player.x > shooter.x:
                shooter.x += 2

            if random.randint(0, 100) < 3:
                enemy_shoot(shooter)

            if player.colliderect(shooter):
                game = False


            for bullet in bullets[:]:
                if shooter.colliderect(bullet):
                    shooter.hp -= 1

                    if bullet in bullets:
                        bullets.remove(bullet)

                    if shooter.hp <= 0:
                        if shooter in spaceshooters:
                            spaceshooters.remove(shooter)
                        break  


        for ebullet in enemy_bullets[:]:
            ebullet.y += 4

            if ebullet.y > HEIGHT:
                enemy_bullets.remove(ebullet)

            if player.colliderect(ebullet):
                game = False



spawn_bugs()


def draw():
    if game:
        screen.blit("space", (0, 0))

        player.draw()

        for bullet in bullets:
            bullet.draw()

        for enemie in bugs:
            enemie.draw()

        for shooter in spaceshooters:
            shooter.draw()


            screen.draw.filled_rect(
                Rect((shooter.x - 25, shooter.y - 40), (50, 5)),
                "red"
            )
            screen.draw.filled_rect(
                Rect((shooter.x - 25, shooter.y - 40), (shooter.hp * (50/30), 5)),
                "green"
            )

        for ebullet in enemy_bullets:
            ebullet.draw()

    else:
        screen.fill("black")
        


pgzrun.go()
