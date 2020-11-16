from tkinter import *
#import os.path
import os
from cryptography.fernet import Fernet


def delete3():
    screen3.destroy()


def delete4():
    screen4.destroy()


def delete5():
    screen5.destroy()


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Welcome")
    screen3.geometry("150x100")
    login_right = Label(screen3, text="Login success")
    login_right.pack()
    login_destroy = Button(screen3, text="Ok", command=delete3)
    login_destroy.pack()
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Welcome To Your Skilltree")
    screen6.geometry("500x250")

def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Wrong")
    screen4.geometry("150x100")
    login_password = Label(screen4, text="Password Error")
    login_password.pack()
    password_destroy = Button(screen4, text="Ok", command=delete4)
    password_destroy.pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Register new User")
    screen5.geometry("150x100")
    login_user = Label(screen5, text="User Error")
    login_user.pack()
    user_destroy = Button(screen5, text="Ok", command=delete5)
    user_destroy.pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    #save_path = '~/PycharmProjects/Skilltree/Users'
    #name_of_file = username_info
    #completeName = os.path.join(save_path, name_of_file)
    file=open(username_info, "w")
    file.write(username_info + "\n" + password_info + "\n")
    file.close()
        
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(screen1, text="Registration Success")


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text=" ").pack()
    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password, show="*")
    password_entry.pack()
    Label(screen1, text=" ").pack()
    Button(screen1, text="Register", height="2", width="30", command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    
    Label(screen2, text="Please enter details below").pack()
    Label(screen2, text=" ").pack()
    
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entry1
    global password_entry1
    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, text=username_verify)
    username_entry1.pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, text = password_verify, show="*")
    password_entry1.pack()
    Label(screen2, text=" ").pack()
    Button(screen2, text="Login", width="10", height="1", command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Welcome")
    screen.configure(bg='darkgrey')
    Label(text="Login or Register", bg="grey", width="300", height="2").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text=" ", bg='darkgrey').pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    screen.mainloop()
