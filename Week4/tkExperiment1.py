from tkinter import *
from playsound import playsound

def hello():
    if label1["text"] == "Hello":
        label1["text"] = "Goodbye"
        label1["image"] = straight
        playsound("Week5\\1302\\sheep.mp3")
    else:
        label1["text"] = "Hello"
        label1["image"] = happy
        playsound("Week5\\1302\\cow.mp3")






wnd = Tk()

wnd.title("Hello world")

straight = PhotoImage(file="Week5\\1302\\face.gif")
happy = PhotoImage(file="Week5\\1302\\happy.gif")
switch = PhotoImage(file="Week5\\1302\\switch.gif")
frame1 = Frame(wnd)
frame1.pack(side="top", padx=20, pady=20)


label1 = Label(frame1, text="Hello this is a label", background="pink", image=happy)
label1.pack(side="left")

button1 = Button(frame1, text="Click me", command=hello, image=switch)
button1.pack(side="left")

button2 = Button(frame1, text="another button")
button2.pack(side="left")
wnd.mainloop()



