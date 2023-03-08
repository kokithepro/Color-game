import tkinter
import random

colors=["Red","Blue","Green","Pink","Black","Yellow","Orange","White","Purple","Brown","Gold","Silver"]

timeleft=30

point = 0



def startGame(event):
    if timeleft==30:
         print("Hi")
         countdown()
    nextColor()

def countdown():
    global timeleft
    if timeleft>0:
        timeleft=timeleft-1
        timetext.config(text="Time left:"+str(timeleft))
        timetext.after(1000,countdown)


def nextColor():
    global point
    global timeleft
    if timeleft>0:
        answer.focus_set()
        if answer.get().lower()==colors[1].lower():
            point=point+1
        answer.delete(0, tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        score.config(text="Score:"+str(point))


label=tkinter.Label(text="", font=('Helvetica',60))
label.pack()
        
window=tkinter.Tk()

window.title("Color Typing Game")
instruction=tkinter.Label(window, text="Type the color of the words!")
instruction.pack()

score=tkinter.Label(window, text="Press enter to start")
score.pack()

timetext=tkinter.Label(window, text="Time left:"+str(timeleft))
timetext.pack()

label=tkinter.Label(window,text="",font=("Helvetical",60))
label.pack()

answer=tkinter.Entry(window)
window.bind('<Return>',startGame)
answer.pack()
answer.focus_set()

window.mainloop


