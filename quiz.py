import pgzrun
import random
WIDTH = 1200
HEIGHT = 1000
titlebox=Rect(0, 0, 1200, 100)
quebox=Rect(0, 120, 800, 100)
timeboxd = Rect(820, 120, 350, 100)
answerbox=Rect(0, 240, 390, 300)
answerbox1=Rect(0, 560, 390, 300)
answerbox2=Rect(410, 240, 390, 300)
answerbox3=Rect(410, 560, 390, 300)
sfb= Rect(820, 240, 350,700)
def draw():
    screen.fill("black")
    screen.draw.filled_rect(titlebox, "blue")
    screen.draw.filled_rect(quebox, "gray")
    screen.draw.filled_rect(timeboxd, "gray")
    screen.draw.filled_rect(answerbox, "#417f91")
    screen.draw.filled_rect(answerbox1, "#417f91")
    screen.draw.filled_rect(answerbox2, "#417f91")
    screen.draw.filled_rect(answerbox3, "#417f91")
    screen.draw.filled_rect(sfb, "#2c661f")
def update():
    pass
pgzrun.go()
