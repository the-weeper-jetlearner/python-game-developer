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
TIMELEFT = 20
gameover = False
file = open("questions.txt","r",encoding="utf8")
questions = []
question = ""
questionindex = 0
for i in file:

  questions.append(i.strip())
def qsucide():
    global questionindex
    global questions
    global question
    question = questions[questionindex].split("|")
qsucide()
def draw():
    screen.fill("black")
    screen.draw.filled_rect(titlebox, "blue")
    screen.draw.textbox("Quiz Time",titlebox)
    screen.draw.filled_rect(quebox, "gray")
    screen.draw.textbox(question[0],quebox)
    screen.draw.filled_rect(timeboxd, "gray")
    screen.draw.textbox(str(TIMELEFT),timeboxd)
    screen.draw.filled_rect(answerbox, "#417f91")
    screen.draw.textbox(question[1],answerbox)
    screen.draw.filled_rect(answerbox1, "#417f91")
    screen.draw.textbox(question[2],answerbox1)
    screen.draw.filled_rect(answerbox2, "#417f91")
    screen.draw.textbox(question[3],answerbox2)
    screen.draw.filled_rect(answerbox3, "#417f91")
    screen.draw.textbox(question[4],answerbox3)
    screen.draw.filled_rect(sfb, "#2c661f")
    screen.draw.textbox("Skip",sfb)
    if gameover == True:
        screen.fill ('red')
        screen.draw.text("you lost!\n you shall now be hacked",(600,500))

def update():
    titlebox.x -= 30
    if titlebox.right < 0:
        titlebox.left = 1200

def updatetime():
    global TIMELEFT
    global gameover
    if TIMELEFT > 0:
        TIMELEFT -= 1
    if TIMELEFT <= 0:
        gameover = True
clock.schedule_interval(updatetime, 1)
pgzrun.go()


