from tkinter import *
import sqlite3

con = sqlite3.connect("user_data.db")
cur = con.cursor()


def close_me(new):
    new.destroy()


def send_data(username, email, number):

    cur.execute("""create table if not exists user_data
                (username text, email text, phonenumber real)""")
    con.commit()

    # get data
    username_ = username.get()
    email_ = email.get()
    number_ = number.get()

    # delete data
    username.delete(0, END)
    email.delete(0, END)
    number.delete(0, END)

    cur.execute("insert into user_data values(?,?,?)",
                (username_, email_, number_))
    con.commit()


def get_window():
    add_w = Toplevel(window)

    label1 = Label(add_w, text="User Details")
    label1.pack()

    search_label = Label(add_w, text="Search")
    search_label.pack()

    field1 = Entry(add_w, width=50, background="white")
    field1.pack()

    panel1 = Text(add_w, width=50, background="white")
    panel1.pack()

    button1 = Button(add_w, text="Go Home", command=lambda: close_me(add_w))
    button1.pack()

    pass


def add_window():
    add_w = Toplevel(window)
    pass

    lbl1 = Label(add_w, text="Add User Details")
    lbl1.pack()

    username_fld = Entry(add_w, width=50, background="white")
    username_fld.pack()

    user_label = Label(add_w, text="Full Name")
    user_label.pack(side="top")

    email_fld = Entry(add_w, width=50, background="white")
    email_fld.pack()

    email_label = Label(add_w, text="Email")
    email_label.pack(side="top")

    number_fld = Entry(add_w, width=50, background="white")
    number_fld.pack()

    number_label = Label(add_w, text="Contact Number")
    number_label.pack(side="top")

    # add a button that will close the child window
    btn1 = Button(add_w, text="Go Home", command=lambda: close_me(add_w))
    btn1.pack(side="bottom")

    button_1 = Button(add_w, text="Submit", command=lambda:
                      send_data(username_fld, email_fld, number_fld))
    button_1.pack()

    # get the focus and do not allow input anywhere else
    add_w.focus_set()
    add_w.grab_set()


window = Tk()
window.title("Home Page")


add_user = PhotoImage(file="Week5\\1302\\add.gif")
search_user = PhotoImage(file="Week5\\1302\\search.gif")
exit = PhotoImage(file="Week5\\1302\\exit.gif")

add_button = Button(window, image=add_user, command=add_window)
add_button.pack(side="top")

search_button = Button(window, image=search_user, command=get_window)
search_button.pack(side="top")

exit_button = Button(window, text="Exit", command=exit, image=exit)
exit_button.pack(side="top")

window.mainloop()
