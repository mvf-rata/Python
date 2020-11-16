from tkinter import *
import sqlite3

# Database
conn = sqlite3.connect('allclothes.db')
c = conn.cursor()

# Create a Table
#c.execute("""CREATE TABLE socks (
#    Quantity INTEGER,
#    Color text,
#    Type text
#    )""")

#c.execute("""CREATE TABLE trousers (
#    Quantity INTEGER,
#    Color text,
#    Type text
#    )""")

#c.execute("""CREATE TABLE shorts (
#    Quantity INTEGER,
#    Color text,
#    Type text
#    )""")


#c.execute("""CREATE TABLE shirts (
#    Quantity INTEGER,
#    Color text,
#    Type text
#    )""")

#c.execute("""CREATE TABLE boxers (
#    Quantity INTEGER,
#    Color text,
#    Type text
#    )""")

#c.execute("""CREATE TABLE pullovers (
#    Quantity INTEGER,
#    Color text,
#    Type text
#    )""")



# Main Window
root = Tk()
root.title('Welcome To The Wardrobe')

# Entry Textboxes
u_name = Entry(root, width=30)
u_name.grid(row=1, column=1)
psswd = Entry(root, width=30, show="*")
psswd.grid(row=2, column=1)

# Label
greeting = Label(root, text="Welcome to the Wardrobe!")
greeting.grid(row=0, column=1)
u_name_label = Label(root, text="Username:")
u_name_label.grid(row=1, column=0)
psswd_label = Label(root, text="Password:")
psswd_label.grid(row=2, column=0)


# defs
def getall():
    show1()
    show2()
    show3()
    show4()
    show5()
    show6()


def show1():
    window2 = Tk()
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM socks")
    items = c.fetchall()
    print_items = ''
    for item in items:
        print_items += str(item) + "\n"
    tabel_label = Label(window2, text="-----Socks------")
    tabel_label.grid(row=2, column=3)
    query_label = Label(window2, text=print_items)
    query_label.grid(row=3, column=3)


def show2():
    window2 = Tk()
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shirts")
    items = c.fetchall()
    print_items = ''
    for item in items:
        print_items += str(item) + "\n"
    tabel_label = Label(window2, text="-----Shirts")
    tabel_label.grid(row=2, column=3)
    query_label = Label(window2, text=print_items)
    query_label.grid(row=3, column=3)


def show3():
    window2 = Tk()
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pullovers")
    items = c.fetchall()
    print_items = ''
    for item in items:
        print_items += str(item) + "\n"
    tabel_label = Label(window2, text="-----Pullovers-----")
    tabel_label.grid(row=2, column=3)
    query_label = Label(window2, text=print_items)
    query_label.grid(row=3, column=3)


def show4():
    window2 = Tk()
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM shorts")
    items = c.fetchall()
    print_items = ''
    for item in items:
        print_items += str(item) + "\n"
    tabel_label = Label(window2, text="-----Shorts-----")
    tabel_label.grid(row=2, column=3)
    query_label = Label(window2, text=print_items)
    query_label.grid(row=3, column=3)


def show5():
    window2 = Tk()
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM trousers")
    items = c.fetchall()
    print_items = ''
    for item in items:
        print_items += str(item) + "\n"
    tabel_label = Label(window2, text="-----Trousers-----")
    tabel_label.grid(row=2, column=3)
    query_label = Label(window2, text=print_items)
    query_label.grid(row=3, column=3)


def show6():
    window2 = Tk()
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM boxers")
    items = c.fetchall()
    print_items = ''
    for item in items:
        print_items += str(item) + "\n"
    tabel_label = Label(window2, text="-----Boxers-----")
    tabel_label.grid(row=2, column=3)
    query_label = Label(window2, text=print_items)
    query_label.grid(row=3, column=3)


def getone():
    window = Tk()
    socks = Button(window, text="Socks", command=show1)
    shirts = Button(window, text="Shirts", command=show2)
    pullovers = Button(window, text="Pullovers", command=show3)
    shorts = Button(window, text="Shorts", command=show4)
    trousers = Button(window, text="Trousers", command=show5)
    boxers = Button(window, text="Boxers", command=show6)

    socks.grid(row=2, column=1)
    shirts.grid(row=3, column=1)
    pullovers.grid(row=4, column=1)
    shorts.grid(row=5, column=1)
    trousers.grid(row=6, column=1)
    boxers.grid(row=7, column=1)


def addone():
    window4 = Tk()
    conn = sqlite3.connect('allclothes.db')
    c = conn.cursor()
    # Entrys
    what = Entry(window4, width=30)
    what.grid(row=2, column=1)
    quantity = Entry(window4, width=30)
    quantity.grid(row=3, column=1)
    color = Entry(window4, width=30)
    color.grid(row=4, column=1)
    type = Entry(window4, width=30)
    type.grid(row=5, column=1)

    # Labels
    what_label = Label(window4, text="What do you want to add:")
    what_label.grid(row=2, column=0)
    quantity_label = Label(window4, text="Quantity:")
    quantity_label.grid(row=3, column=0)
    color_label = Label(window4, text="Color:")
    color_label.grid(row=4, column=0)
    type_label = Label(window4, text="TYPE:")
    type_label.grid(row=5, column=0)

    def submit():
        if what.get() == "socks" or "Socks":
            statement = ("INSERT INTO socks VALUES (?, ?, ?)")
            c.execute(statement, (quantity.get(), color.get(), type.get()))
            conn.commit()
        if what.get() == "shorts" or "Shorts":
            statement = ("INSERT INTO shorts VALUES (?, ?, ?)")
            c.execute(statement, (quantity.get(), color.get(), type.get()))
            conn.commit()
        if what.get() == "shirts" or "Shirts":
            statement = ("INSERT INTO shirts VALUES (?, ?, ?)")
            c.execute(statement, (quantity.get(), color.get(), type.get()))
            conn.commit()
        if what.get() == "boxers" or "Boxers":
            statement = ("INSERT INTO boxers VALUES (?, ?, ?)")
            c.execute(statement, (quantity.get(), color.get(), type.get()))
            conn.commit()
        if what.get() == "trousers" or "Trousers":
            statement = ("INSERT INTO trousers VALUES (?, ?, ?)")
            c.execute(statement, (quantity.get(), color.get(), type.get()))
            conn.commit()
        if what.get() == "pullovers" or "Pullovers":
            statement = ("INSERT INTO pullovers VALUES (?, ?, ?)")
            c.execute(statement, (quantity.get(), color.get(), type.get()))
            conn.commit()
        else:
            no = Label(window4, text="This table doesnt exist! Check your spelling!")
            no.grid(row=6, column=1, columnspan=2)

        what.delete(0, END)
        quantity.delete(0, END)
        color.delete(0, END)
        type.delete(0, END)

    submit_btn = Button(window4, text="Submit", command=submit)
    submit_btn.grid(row=6, column=1)


def delete():
    window5 = Tk()
    global whatd
    global colord
    global typed
    intro = Label(window5, text="Here you can delete and take clothes out of your Wardrobe.")
    intro.grid(row=0, column=0, columnspan=4)

    whatd = Entry(window5, width=30)
    whatd.grid(row=1, column=2, columnspan=2)
    whatd_label = Label(window5, text="What do you want to delete?")
    colord = Entry(window5, width=30)
    colord.grid(row=2, column=2, columnspan=2)
    colord_label = Label(window5, text="Color:")
    colord_label.grid(row=2, column=0)
    typed = Entry(window5, width=30)
    typed.grid(row=3, column=2, columnspan=2)
    typed_label = Label(window5, text="Type:")
    typed_label.grid(row=3, column=0)

    getone()

    doit = Button(window5, text="Do it!", command=DOIT)
    doit.grid(row=4, column=2)


def DOIT():
    if whatd.get() == "socks":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement4 = ("""DELETE from socks WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (colord.get(), typed.get()))
        conn.commit()
        conn.close()
        print("!DELETED!")

    if whatd.get() == "trousers":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement4 = ("""DELETE from trousers WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (colord.get(), typed.get()))
        conn.commit()
        conn.close()
        print("!DELETED!")

    if whatd.get() == "boxers":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement4 = ("""DELETE from boxers WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (colord.get(), typed.get()))
        conn.commit()
        conn.close()
        print("!DELETED!")

    if whatd.get() == "shorts":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement4 = ("""DELETE from shorts WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (colord.get(), typed.get()))
        conn.commit()
        conn.close()
        print("!DELETED!")

    if whatd.get() == "pullovers":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement4 = ("""DELETE from pullovers WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (colord.get(), typed.get()))
        conn.commit()
        conn.close()
        print("!DELETED!")

    if whatd.get() == "shirts":
        conn = sqlite3.connect('allclothes.db')
        c = conn.cursor()
        statement4 = ("""DELETE from shirts WHERE Color = (?) AND Type = (?)""")
        c.execute(statement4, (colord.get(), typed.get()))
        conn.commit()
        conn.close()
        print("!DELETED!")


# Enter def
def enter():
    login()
    # Clear Text Boxes
    # u_name.delete(0, END)
    # psswd.delete(0, END)
    if success is True:
        # New Window
        window = Tk()
        window.title('Wardrobe')
        greeting2 = Label(window, text="Hello" + " " + u_name.get() + "!")
        greeting2.grid(row=0, column=0, columnspan=5)

        # Buttons
        showall = Button(window, text="Get All", command=getall)
        showone = Button(window, text="Get One", command=getone)
        plusone = Button(window, text="Add One", command=addone)
        take = Button(window, text="Delete", command=delete)

        showall.grid(row=1, column=0)
        showone.grid(row=1, column=1)
        plusone.grid(row=1, column=2)
        take.grid(row=1, column=3)


# Enter Button
enter_btn = Button(root, text="Enter", command=enter)
enter_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


def login():
    credential = {"rata": "twiisker", "buck": "alpha"}
    global success
    success = False
    for i in range(3):
        username = u_name.get()
        password = psswd.get()
        if credential.get(username) == password:
            success = True
            break
        else:
            u_name.delete(0, END)
            psswd.delete(0, END)
        if not success:
            window1 = Tk()
            window1.title('...')
            failed = Label(window1, text=u_name.get() + " " + "read README.txt first")
            failed.pack()


root.mainloop()
