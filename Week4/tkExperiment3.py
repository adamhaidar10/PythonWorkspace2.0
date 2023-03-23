from tkinter import *

# close the child window
def closeme(new):
    new.destroy()


# function to create a new child window
def child1():
    # create a window that is a child of the parent window
    new = Toplevel(wnd)

    lbl1 = Label(new, text="Hello from child 1")
    lbl1.pack()

    # add a button that will close the child window
    btn2 = Button(new, text="Close me", command=lambda: closeme(new))
    btn2.pack()

    # get the focus and do not allow input anywhere else
    new.focus_set()
    new.grab_set()

def child2():
    pass


# create a new parent window
wnd = Tk()
wnd.title("Parent window")


# add a button that will open a child window
btn1 = Button(wnd, text="Child 1", command=child1)
btn1.pack()

btn2 = Button(wnd, text="Child 2", command=child2)
btn2.pack()

# execute the main loop
wnd.mainloop()