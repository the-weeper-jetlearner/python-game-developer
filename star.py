import pgzrun
import random

WIDTH = 1200
HEIGHT = 1000

items = []

level = 1
speed = 3
stars_needed = 5
score = 0

gameover = False
gamecomplete = False


def make_level():
    global items

    items = []

    
    player = Actor("blue")
    player.pos = (WIDTH / 2, HEIGHT - 80)
    player.type = "player"
    items.append(player)


    
    for i in range(stars_needed):
        star = Actor("green")
        star.pos = (
            random.randint(50, WIDTH - 50),
            random.randint(-500, -50)
        )
        star.type = "star"
        items.append(star)


    
    for i in range(level):
        bad = Actor(random.choice(["red", "purple", "orange"]))
        bad.pos = (
            random.randint(50, WIDTH - 50),
            random.randint(-500, -50)
        )
        bad.type = "bad"
        items.append(bad)



def update():
    global score
    global level
    global speed
    global stars_needed
    global gameover
    global gamecomplete


    if gameover or gamecomplete:
        return


    player = items[0]


    
    if keyboard.left:
        player.x -= 6

    if keyboard.right:
        player.x += 6


    
    if player.x < 0:
        player.x = 0

    if player.x > WIDTH:
        player.x = WIDTH



   
    for item in items[1:]:

        item.y += speed


        
        if item.y > HEIGHT:
            item.y = -50
            item.x = random.randint(50, WIDTH - 50)



       
        if player.colliderect(item):

            if item.type == "star":
                score += 1

                item.y = -50
                item.x = random.randint(50, WIDTH - 50)



            elif item.type == "bad":
                gameover = True



  
    if score >= stars_needed:

        level += 1
        speed += 1
        stars_needed += 5


        if level > 5:
            gamecomplete = True

        else:
            make_level()



def draw():

    screen.fill("white")


    if gameover:

        screen.draw.text(
            "YOU LOST!",
            center=(WIDTH/2, HEIGHT/2),
            fontsize=80,
            color = "black"
        )


    elif gamecomplete:

        screen.draw.text(
            "YOU WON!",
            center=(WIDTH/2, HEIGHT/2),
            fontsize=80,
            color = "black"
        )


    else:

        for item in items:
            item.draw()


        screen.draw.text(
            "Score: " + str(score),
            (20,20),
            fontsize=40
        )


        screen.draw.text(
            "Level: " + str(level),
            (20,60),
            fontsize=40
        )



make_level()

pgzrun.go()