from tkinter import *
#import os.path
import os
from cryptography.fernet import Fernet

def destroy8():
    screen8.destroy()
    screen7.destroy()

def saved():
    global screen8
    screen8 = Toplevel(screen)
    screen8.title("Saved")
    screen8.geometry("150x50")
    Label(screen8, text="Note has been saved").pack()
    Button(screen8, text="Ok", command=destroy8).pack()


def save():
    filename = raw_filename.get()
    notes = raw_notes.get()

    data = open(filename, 'w')
    data.write(notes)
    data.close()

    saved()

def create_notes():
    global raw_filename
    raw_filename = StringVar()
    global raw_notes
    raw_notes = StringVar()
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Notes")
    screen7.geometry("250x400")
    Label(screen7, text="Pls enter a Filename").pack()
    Entry(screen7, textvariable = raw_filename).pack()
    Label(screen7, text="Pls enter the Notes").pack()
    Entry(screen7, textvariable = raw_notes).pack()
    Button(screen7, text="Save", command=save).pack()


def show_note():
    filename1 = raw_filename1.get()
    data = open(filename1, 'r')
    data1 = data.read()
    screen10 = Toplevel(screen)
    screen10.title("The Note")
    screen10.geometry("450x400")
    Label(screen10, text=data1).pack()
    

def view_notes():
    screen9 = Toplevel(screen)
    screen9.title("View Notes")
    screen9.geometry("400x150")
    global all_files
    all_files = os.listdir()
    Label(screen9, text="Choose a file from below").pack()
    Label(screen9, text = all_files).pack()
    global raw_filename1    
    raw_filename1 = StringVar()
    Entry(screen9, textvariable=raw_filename1).pack()
    Button(screen9, text="Ok", command=show_note).pack()


def destroy12():
    screen12.destroy()
    screen11.destroy()


def delete_note1():
    global screen12
    filename3 = raw_filename2.get()
    os.remove(filename3)
    screen12 = Toplevel(screen)
    screen12.title("Delete")
    screen12.geometry("150x100")
    Label(screen12, text=filename3 + " removed").pack()
    Button(screen12, text="Ok", command=destroy12).pack()



def delete_notes():
    global screen11
    screen11 = Toplevel(screen)
    screen11.title("Delete Notes")
    screen11.geometry("400x150")
    global all_files
    all_files = os.listdir()
    Label(screen11, text="Choose a file from below").pack()
    Label(screen11, text = all_files).pack()
    global raw_filename2    
    raw_filename2 = StringVar()
    Entry(screen11, textvariable=raw_filename2).pack()
    Button(screen11, text="Ok", command=delete_note1).pack()

def login_success():
    Label(screen2, text="Login Successfull", fg="green").pack()
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Dashboard")
    screen6.geometry("150x150")
    Button(screen6, text="Create Note", command=create_notes).pack()
    Button(screen6, text="View Note", command=view_notes).pack()
    Button(screen6, text="Delete Note", command=delete_notes).pack()
    screen2.destroy()
    

def delete3():
    screen3.destroy()


def delete4():
    screen4.destroy()


def delete5():
    screen5.destroy()


def password_not_recognized():
    Label(screen2, text="Wrong Password", fg="red").pack()


def user_not_found():
    Label(screen2, text="User not found", fg = "red").pack()


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
    screen.title("Welcome To Your Notes")
    screen.configure(bg='darkblue')
    Label(text="Login or Register", fg="white", bg="darkblue", width="300", height="2").pack()
    Button(text="Login", bg="darkgrey", height="2", width="30", command=login).pack()
    Label(text=" ", bg='darkblue').pack()
    Button(text="Register", bg="darkgrey", height="2", width="30", command=register).pack()
    screen.mainloop()

main_screen()