import pgzrun
import math

WIDTH = 1000
HEIGHT = 800

def draw():
    screen.fill("black")

    # Fade value oscillates between 0 and 1
    t = (math.sin(time.time() * 1.5) + 1) / 2

    # Blue → Purple interpolation
    # Blue   = (0, 0, 255)
    # Purple = (128, 0, 128)
    r = int(0   + (128 - 0)   * t)
    g = 0
    b = int(255 + (128 - 255) * t)

    fade_color = (r, g, b)

    w = 900
    h = 200

    for i in range(25):
        rect = Rect((0, 0), (w, h))
        rect.center = (500, 400)
        screen.draw.rect(rect, fade_color)
        w -= 28
        h += 25

def update():
    pass

import time
pgzrun.go()
