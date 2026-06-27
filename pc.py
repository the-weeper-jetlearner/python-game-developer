import random
import pgzrun
import time
import string


WIDTH = 1000
HEIGHT = 1000

gamestate = 7



level = 0
total_levels = 10
score = 0
nodedrawa = Rect(100, 250, 350, 550)
nodedrawb = Rect(550, 250, 350, 550)
cipher_shift = 0
encrypted_word = ""
answer = ""
player_input = ""

start_time = 0
time_limit = 900


words = [
    "computer", "logic", "python", "game", "keyboard",
    "screen", "code", "robot", "mouse", "internet",
    "program", "software", "hardware", "processor", "memory",
    "binary", "digital", "system", "network", "server",
    "database", "website", "browser", "application", "technology",
    "algorithm", "variable", "function", "coding", "developer",
    "engineer", "machine", "device", "phone", "tablet",
    "laptop", "monitor", "camera", "speaker", "microphone",
    "wire", "cable", "signal", "power", "battery",
    "electric", "energy", "science", "math", "number",
    "zero", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "space", "planet", "star", "moon", "earth",
    "rocket", "alien", "galaxy", "universe", "orbit",
    "future", "time", "clock", "second", "minute",
    "hour", "day", "night", "light", "dark",
    "shadow", "fire", "water", "air", "earth",
    "stone", "metal", "gold", "silver", "diamond",
    "tree", "forest", "river", "ocean", "mountain",
    "animal", "bird", "fish", "dog", "cat",
    "wolf", "lion", "tiger", "dragon", "monster",
    "hero", "villain", "battle", "war", "peace",
    "sword", "shield", "armor", "weapon", "castle",
    "king", "queen", "prince", "princess", "knight",
    "magic", "spell", "power", "secret", "mystery",
    "door", "key", "lock", "escape", "trap",
    "mission", "quest", "level", "challenge", "puzzle",
    "answer", "question", "problem", "solution", "idea",
    "brain", "mind", "think", "learn", "school",
    "book", "paper", "story", "word", "letter",
    "music", "sound", "song", "movie", "video",
    "picture", "image", "color", "shape", "design",
    "create", "build", "make", "fix", "repair",
    "open", "close", "start", "stop", "run",
    "jump", "move", "walk", "fight", "win",
    "lose", "fast", "slow", "strong", "smart",
    "quick", "hidden", "secret", "danger", "safe",
    "enemy", "friend", "team", "alone", "leader",
    "explore", "discover", "find", "search", "lost",
    "travel", "journey", "road", "map", "world",
    "city", "house", "room", "doorway", "window",
    "chair", "table", "food", "drink", "water",
    "coffee", "apple", "orange", "banana", "fruit"
]

def caesar_encrypt(text, shift):

    result = ""

    for char in text:

        if char in string.ascii_lowercase:

            pos = ord(char) - ord("a")
            pos = (pos + shift) % 26

            result += chr(pos + ord("a"))

        else:
            result += char

    return result



def new_level():

    global encrypted_word
    global answer
    global cipher_shift


    answer = random.choice(words)

    cipher_shift = random.randint(1,25)

    encrypted_word = caesar_encrypt(
        answer,
        cipher_shift
    )



def update():
    pass




def lv1():

    global gamestate

    if gamestate == 1:
        gamestate = 2



def lv2():

    global gamestate

    if gamestate == 2:
        gamestate = 3



def lv3():

    global gamestate

    if gamestate == 3:
        gamestate = 4



def lv4():

    global gamestate

    if gamestate == 4:
        gamestate = 5

def level2():
    global gamestate
    if gamestate == 7:
        time.sleep(1)
        gamestate = 8


        

def start_game():

    global gamestate
    global level
    global start_time


    gamestate = 6

    level = 1

    start_time = time.time()

    new_level()





def on_mouse_down(pos):

    if gamestate == 5:


        

        if 350 < pos[0] < 650 and 500 < pos[1] < 580:

            start_game()





def on_key_down(key):

    global player_input
    global level
    global score
    global gamestate
    global start_time



    if gamestate == 6:



        

        if key == keys.RETURN:


            if player_input.lower() == answer:


                score += 1

                level += 1


                if level > total_levels:

                    gamestate = 7


                else:

                    new_level()



            else:

               

                start_time -= 10



            player_input = ""




        elif key == keys.BACKSPACE:


            player_input = player_input[:-1]



        else:


            if len(player_input) < 20:

                player_input += key.name.lower()

def nodegame():
    pass


def draw():

    global gamestate



    

    screen.blit("pc",(0,0))





    if gamestate == 1:


        screen.draw.text(
            "THIS IS A GAME ABOUT A DUDE AT A PC",
            (250,200),
            fontsize=40
        )





    if gamestate == 2:


        screen.draw.text(
            "HE GOT TRAPPED IN A PC",
            (300,300),
            fontsize=40
        )





    if gamestate == 3:


        screen.draw.text(
            "YOUR TASK: GET HIM OUT",
            (300,400),
            fontsize=40
        )





    if gamestate == 4:


        screen.draw.text(
            "USING LOGIC...",
            (400,500),
            fontsize=40
        )









    if gamestate == 5:



        screen.draw.text(
            "PC ESCAPE SYSTEM",
            (330,180),
            fontsize=45,
            color=(180,180,140)
        )



        


        screen.draw.filled_rect(
            Rect(350,500,300,80),
            (60,60,60)
        )


        screen.draw.rect(
            Rect(350,500,300,80),
            (150,150,120)
        )



        screen.draw.text(
            "START GAME",
            (390,525),
            fontsize=35,
            color=(180,180,140)
        )







   


    if gamestate == 6:



        remaining = time_limit - int(
            time.time()-start_time
        )


        screen.draw.text(
            f"LEVEL {level}/10",
            (50,50),
            fontsize=40
        )


        screen.draw.text(
            f"TIME LEFT {remaining}",
            (50,100),
            fontsize=35
        )



        screen.draw.text(
            "DECODE THIS:",
            (350,250),
            fontsize=40
        )


        screen.draw.text(
            encrypted_word.upper(),
            (400,350),
            fontsize=70
        )



        screen.draw.text(
            "ANSWER: "+player_input,
            (300,500),
            fontsize=40
        )



        if remaining <= 0:

            gamestate = 7









    if gamestate == 7:



        screen.draw.text(
            f"READY FOR A SITUATION, SCORE {score}/10",
            (250,450),
            fontsize=50
        )
        gamestate = 8
    if gamestate == 8:
        screen.fill("#343944")
        screen.draw.filled_rect(nodedrawa, "#D1BC26")
        screen.draw.filled_rect(nodedrawb, "#D1BC26")






clock.schedule(lv1,1)
clock.schedule(lv2,2)
clock.schedule(lv3,3)
clock.schedule(lv4,4)



pgzrun.go()
