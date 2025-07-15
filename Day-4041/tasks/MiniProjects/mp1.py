# 🔧 1. Login and Registration System
# Goal: Allow users to register with a username, email, and password and then log in.
# Requirements:
# •	Use Entry widgets for inputs.
# •	Validate email using regex.
# •	Password field should mask characters (show="*").
# •	Use pack() or grid() for layout.
# •	Show login success or failure using Label.
# •	Save login data in a dictionary or text file (basic implementation).

import tkinter as tk
import re
import os

root=tk.Tk()
root.geometry("500x400")

USER_FILE="users.txt"


def save_users(username, email, password):
    with open(USER_FILE, "a") as file:
        file.write(f"{username}, {email}, {password}\n")

def load_users():
    users={}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as file:
            for line in file:
                parts=line.strip().split(",")
                if len(parts)==3:
                    username, email, password=[p.strip() for p in parts]
                    users[email]=(username, password)
    return users

def is_valid_email(email):
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def register():
    username=name_entry.get()
    email=email_entry.get().strip().lower()
    password=password_entry.get() 

    if not username or not email or not password:
        message_label.config(text="All fields are required.", fg="red")
        return
    if not is_valid_email(email):
        message_label.config(text="Invalid Email. Please enter valid email.", fg="red")
        return
    if email in users:
        message_label.config(text="Email already exists.", fg="red")
        return
    users[email]=(username, password)
    save_users(username, email, password)
    message_label.config(text="Registration successful!", fg="green")

def login():
    email=email_entry.get()
    password=password_entry.get()
    if email in users and users[email][1]==password:
        message_label.config(text=f"Welcome, {users[email][0]}", fg="green")
    else:
        message_label.config(text="Login failed. Check your email or password.", fg="red")

users=load_users()

name_label=tk.Label(root, text="User Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry=tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label=tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry=tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

password_label=tk.Label(root, text="Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry=tk.Entry(root, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

register_btn=tk.Button(root, text="Register", command=register)
register_btn.grid(row=3, column=1, pady=10)

login_btn=tk.Button(root, text="Login", command=login)
login_btn.grid(row=4, column=1, pady=10)

message_label=tk.Label(root, text="")
message_label.grid(row=5, column=1, pady=20)

root.mainloop()

