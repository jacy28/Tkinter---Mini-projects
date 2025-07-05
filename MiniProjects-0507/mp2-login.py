# 2. Login and Welcome App
# Goal: Login form that verifies input and opens a welcome window.
# Requirements:
# •	Use two Entry widgets (username, password).
# •	Mask password using show="*".
# •	On button click, check credentials.
# •	Use .title() and .geometry() to manage window.
# •	On success, open a new window with dynamic Label.

import tkinter as tk
from tkinter import messagebox

Valid_username="Admin"
Valid_password="1234"

def check_login():
    username=username_entry.get()
    password=password_entry.get()

    if username == Valid_username and password == Valid_password:
        open_welcome_window(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_welcome_window(username):
    welcome_window = tk.Toplevel(root)
    welcome_window.title("Welcome")
    welcome_window.geometry("300x150")
    
    welcome_label = tk.Label(welcome_window, text=f"Welcome, {username}!", font=("Arial", 14))
    welcome_label.pack(expand=True)
        
root=tk.Tk()
root.title("Login window")
root.geometry("500x500")

username_label=tk.Label(root, text="User Name:", padx=10, pady=20)
username_label.pack()
username_entry=tk.Entry(root)
username_entry.pack()

password_label=tk.Label(root, text="Password:", padx=10, pady=20)
password_label.pack()
password_entry=tk.Entry(root, show="*")
password_entry.pack()

login_btn=tk.Button(root, text="Login", command=check_login)
login_btn.pack(pady=20)

root.mainloop()
