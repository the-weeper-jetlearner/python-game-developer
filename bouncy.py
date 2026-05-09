import pgzrun
import random

WIDTH = 512
HEIGHT = 554

player = Actor("ship")
player.pos = (256, 275)

enemiesImg = ["greenenemy", "greyenemy", "redenemy", "blueenemy"]

enemies = []
explosions = []
doom_explosions = []

dashing = False

map_health = 100
game_over = False
doom_active = False
doom_timer = 0


def spawn_enemie():
    img = random.choice(enemiesImg)
    enemy = Actor(img)

    enemy.speed = random.randint(1, 3)
    enemy.timer = 0

    enemies.append(enemy)

    if img == "greenenemy":
        enemy.pos = (0, 0)
    elif img == "greyenemy":
        enemy.pos = (512, 554)
    elif img == "blueenemy":
        enemy.pos = (512, 0)
    elif img == "redenemy":
        enemy.pos = (0, 554)


clock.schedule_interval(spawn_enemie, 0.7)


def on_mouse_down(pos):
    global dashing

    dashing = True

    animate(
        player,
        angle=player.angle_to(pos) - 90,
        duration=0.7
    )

    animate(
        player,
        pos=pos,
        duration=0.7,
        tween="bounce_end",
        on_finished=stop_dash
    )


def stop_dash():
    global dashing
    dashing = False



def create_explosion(pos):
    explosion = Actor("explosion1")
    explosion.pos = pos
    explosion.frame = 1
    explosion.timer = 0
    explosions.append(explosion)


def update_explosions():

    for explosion in explosions[:]:
        explosion.timer += 1

        if explosion.timer % 5 == 0:
            explosion.frame += 1

            if explosion.frame > 6:
                explosions.remove(explosion)
            else:
                explosion.image = f"explosion{explosion.frame}"


    for explosion in doom_explosions[:]:
        explosion.timer += 1

        if explosion.timer % 3 == 0:
            explosion.frame += 1

            if explosion.frame > 6:
                doom_explosions.remove(explosion)
            else:
                explosion.image = f"explosion{explosion.frame}"


def trigger_doom():
    global game_over, doom_active, doom_timer

    game_over = True
    doom_active = True
    doom_timer = 0

    enemies.clear()
    explosions.clear()


def update():
    global map_health, doom_timer


    if game_over:
        update_explosions()

        if doom_active:
            doom_timer += 1

            
            if doom_timer % 5 == 0:
                explosion = Actor("explosion1")
                explosion.pos = (
                    random.randint(0, WIDTH),
                    random.randint(0, HEIGHT)
                )
                explosion.frame = random.randint(1, 6)
                explosion.timer = 0
                doom_explosions.append(explosion)

            if doom_timer > 300:  
                quit()

        return


    for enemy in enemies[:]:
        dx = player.x - enemy.x
        dy = player.y - enemy.y
        distance = (dx**2 + dy**2) ** 0.5

        if distance != 0:
            dx /= distance
            dy /= distance
            enemy.x += dx * enemy.speed
            enemy.y += dy * enemy.speed

        
        if dashing and player.colliderect(enemy):
            create_explosion((enemy.x, enemy.y))
            enemies.remove(enemy)
            continue

        
        enemy.timer += 1

        if enemy.timer > 120:
            map_health -= 5
            enemy.timer = 0

        if map_health <= 0:
            trigger_doom()
            return

    update_explosions()



def draw():
    screen.blit("map", (0, 0))

    for enemy in enemies:
        enemy.draw()

    for explosion in explosions:
        explosion.draw()

    for explosion in doom_explosions:
        explosion.draw()

    player.draw()

    screen.draw.text(
        f"MAP HEALTH: {map_health}%",
        (10, 10),
        color="white"
    )


pgzrun.go()