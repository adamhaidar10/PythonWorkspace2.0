from playsound import playsound
from tkinter import *


def chicken():
    playsound("Week5\\1302\\chicken.mp3")


def sheep():
    playsound("Week5\\1302\\sheep.mp3")


def cow():
    playsound("Week5\\1302\\cow.mp3")


wnd = Tk()

wnd.title("Farmyard Sounds")

cow = PhotoImage(file="Week5\\1302\\cow.gif")

sheep = PhotoImage(file="Week5\\1302\\sheep.gif")

chicken = PhotoImage(file="Week5\\1302\\chicken.gif")

frame1 = Frame(wnd)
frame1.pack(side="top", padx=20, pady=20)

label1 = Label(frame1, text="These are the sounds of the farm")
label1.pack()

button1 = Button(frame1, text="cow", image=cow, height=250, width=250,
                 command=cow,
                 compound="top")
button1.pack(side="left")


button2 = Button(frame1, image=chicken, height=250, width=250, command=chicken)
button2.pack(side="left")


button3 = Button(frame1, image=sheep, height=250, width=250, command=sheep)
button3.pack(side="left")

wnd.mainloop()
