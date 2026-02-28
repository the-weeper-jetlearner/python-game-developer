import random
from tkinter import *
pipes = {
    '1':'yesssss',
    '2':'i decline',
    '3':'you will try to lock pick and end up in solidary confinement',
    '4':'you will become rich, in bird poop',
    '5':'you will fall into a pit this afternoon',
    '6':'You will find gold, after they buired you',
    '7':'you will get a mug of hot coffee, sorry, i cannot display when you wil :)'
}
#print(pipes.keys())
#print(pipes.values())
#print(pipes['5'])
#del(pipes['4'])
#print(pipes)

#pipes[1] = 'doll'

#for key in pipes.keys():
#    print(key,pipes[key])

#if '1' in pipes:
#    print('s')




#GUI starts
window = Tk()
window.title('VARIABLE clicker')
window.geometry('500x500')
window.config(background='white')
def game():
    numbers = random.choice('1234567')
    text1.config(text=pipes[numbers])
    del(pipes[numbers])
variable = Button(text='click me for dumb decisions', command= game).place (x=150, y=250)
text1=Label(window,text='')
text1.place (x=100, y=350)
window.mainloop()
