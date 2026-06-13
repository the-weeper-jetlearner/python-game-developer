import pgzrun

WIDTH = 1200
HEIGHT = 1000

# Boxes
titlebox = Rect(0, 0, 1200, 100)
quebox = Rect(0, 120, 800, 100)
timeboxd = Rect(820, 120, 350, 100)

answerbox = Rect(0, 240, 390, 300)
answerbox1 = Rect(0, 560, 390, 300)
answerbox2 = Rect(410, 240, 390, 300)
answerbox3 = Rect(410, 560, 390, 300)

sfb = Rect(820, 240, 350, 700)

TIMELEFT = 20
gameover = False
score = 0
questionindex = 0

# Load questions
with open("questions.txt", "r", encoding="utf8") as file:
    questions = [line.strip() for line in file if line.strip()]

question = []


def load_question():
    global question
    global questionindex

    if questionindex < len(questions):
        question = questions[questionindex].split("|")


load_question()


def draw():
    screen.fill("black")

    if gameover:
        screen.fill("red")

        screen.draw.text(
            f"Game Over!\n\nScore: {score}/{len(questions)}",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=70,
            color="white",
        )
        return

    # Title
    screen.draw.filled_rect(titlebox, "blue")
    screen.draw.textbox(
        "Quiz Time",
        titlebox,
        color="white"
    )

    # Question
    screen.draw.filled_rect(quebox, "gray")
    screen.draw.textbox(
        question[0],
        quebox,
        color="black"
    )

    # Timer
    screen.draw.filled_rect(timeboxd, "gray")
    screen.draw.textbox(
        f"Time Left: {TIMELEFT}",
        timeboxd,
        color="black"
    )

    # Answers
    screen.draw.filled_rect(answerbox, "#417f91")
    screen.draw.textbox(question[1], answerbox)

    screen.draw.filled_rect(answerbox1, "#417f91")
    screen.draw.textbox(question[2], answerbox1)

    screen.draw.filled_rect(answerbox2, "#417f91")
    screen.draw.textbox(question[3], answerbox2)

    screen.draw.filled_rect(answerbox3, "#417f91")
    screen.draw.textbox(question[4], answerbox3)

    # Skip button
    screen.draw.filled_rect(sfb, "#2c661f")
    screen.draw.textbox("SKIP", sfb, color="white")


def update():
    # Move title across screen
    titlebox.x -= 5

    if titlebox.right < 0:
        titlebox.left = WIDTH


def updatetime():
    global TIMELEFT, gameover

    if not gameover:
        TIMELEFT -= 1

        if TIMELEFT <= 0:
            gameover = True


clock.schedule_interval(updatetime, 1)


def next_question():
    global questionindex
    global TIMELEFT
    global gameover

    questionindex += 1

    if questionindex >= len(questions):
        gameover = True
        return

    TIMELEFT = 20
    load_question()


def on_mouse_down(pos):
    global score
    global gameover

    if gameover:
        return

    try:
        # LAST item in line is always the correct answer number
        correct = int(question[-1])
    except ValueError:
        print("Invalid question format:", question)
        gameover = True
        return

    chosen = None

    if answerbox.collidepoint(pos):
        chosen = 1

    elif answerbox1.collidepoint(pos):
        chosen = 2

    elif answerbox2.collidepoint(pos):
        chosen = 3

    elif answerbox3.collidepoint(pos):
        chosen = 4

    elif sfb.collidepoint(pos):
        next_question()
        return

    if chosen is None:
        return

    # Check answer
    if chosen == correct:
        score += 1
        next_question()
    else:
        gameover = True


pgzrun.go()
