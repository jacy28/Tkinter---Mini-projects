# 3. Login & Welcome Screen
# Objective: Create a login window and redirect on success.
# Features:
# •	Two Entry fields for username and password (with show="*").
# •	Button triggers validation function.
# •	Validate credentials against hardcoded values.
# •	On success, show another Label window with geometry() & updated title.
# •	Use .place() to center login form.

import tkinter as tk
from tkinter import messagebox

VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        root.destroy()  
        open_welcome_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def open_welcome_window():
    welcome = tk.Tk()
    welcome.title("Welcome")
    welcome.geometry("300x200")

    welcome_label=tk.Label(welcome, text=f"Welcome, {VALID_USERNAME}!", font=("Arial", 14))
    welcome_label.pack(expand=True)

    welcome.mainloop()


root = tk.Tk()
root.title("Login")
root.geometry("300x200")

username_label = tk.Label(root, text="Username:")
username_label.place(x=50, y=50)
username_entry = tk.Entry(root)
username_entry.place(x=130, y=50)


password_label = tk.Label(root, text="Password:")
password_label.place(x=50, y=80)
password_entry = tk.Entry(root, show="*")
password_entry.place(x=130, y=80)


login_button = tk.Button(root, text="Login", command=login)
login_button.place(x=130, y=120)

root.mainloop()
