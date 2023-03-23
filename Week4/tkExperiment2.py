from tkinter import *
# functin that  gets value from field and adds to panel
def addtopanel():
    s = fld1.get()
    fld1.delete(0, END)
    panl1.insert(END, s + "\n")

# function that clears content of panel   
def clearpanel():
    panl1.delete(1.0, END)
# closes program
def exitprogram():
    wnd.destroy()
    exit()


# create a tkinter instance
wnd = Tk()
wnd.title("Interactive program")
# create a frame to hold my objects
frame1 = Frame(wnd)

frame1.pack(side="top", padx=20, pady=20)
# fill frame with controls
label1 = Label(frame1, text="Type something")
label1.pack()

fld1 = Entry(frame1, width=50, background="white")
fld1.pack()


button1 = Button(frame1, text="Now click here", command=addtopanel)
button1.pack()


panl1 = Text(frame1, width=50, background="white")
panl1.pack()

button2 = Button(frame1, text="Clear panel", command=clearpanel)
button2.pack()


button3 = Button(frame1, text="Exit", command=exitprogram)
button3.pack()
# start main loop
wnd.mainloop()