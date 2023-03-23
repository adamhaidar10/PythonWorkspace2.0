import re
from tkinter import *

regex = r"[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} [0-9][A-Z]{2}"

def check():
    s = fld1.get()
    print(s)
    if re.match(regex, s):
        print("The postcode entered is correct")
        text = f"{s} is a valid postcode"
        pnl1.insert(END, text + "\n")
        fld1.delete(0, END)
    else:
        text = f"{s} is an ivalid postcode"
        pnl1.insert(END, text + "\n")
        fld1.delete(0, END)

def clearpanel():
    pnl1.delete(1.0, END)

def exitprogram():
    wnd.destroy()
    exit()

# check("SE15 6FH")

wnd = Tk()
wnd.title("Postcode checker")

frame1 = Frame(wnd)
frame1.pack(side="top", padx=20, pady=20)

lbl1 = Label(frame1, text="Type in a Postcode")
lbl1.pack()

fld1 = Entry(frame1, width=50, background="white")
fld1.pack()

btn1 = Button(frame1, text="Submit", command=check)
btn1.pack()

pnl1 = Text(frame1, width=50, background="white")
pnl1.pack()

btn2 = Button(frame1, text="Clear panel", command=clearpanel)
btn2.pack()

btn3 = Button(frame1, text="exit", command=exitprogram)
btn3.pack()

wnd.mainloop()