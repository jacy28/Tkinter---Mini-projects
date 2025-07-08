# 1.	Simple Login Form
# Username and password fields (Entry), labels, and a Login button. 
# Show a welcome message if the username/password matches a preset value.

import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Login Form")
root.geometry("500x400")
valid_username="admin"
valid_password="1234"
def login():
    username=username_entry.get()
    password=password_entry.get()

    if valid_username==username and valid_password==password:
        messagebox.showinfo("Login successful", f"Welcome, {username}")
    else:
        messagebox.showerror("Login failed", "Please enter valid username & password.")

username_label=tk.Label(root, text="User Name:")
username_label.pack(padx=10, pady=10)
username_entry=tk.Entry(root)
username_entry.pack(padx=10, pady=10)
password_label=tk.Label(root, text="Password:")
password_label.pack(padx=10, pady=10)
password_entry=tk.Entry(root, show="*")
password_entry.pack(padx=10, pady=10)
btn=tk.Button(root, text="Login", command=login)
btn.pack(pady=20)
root.mainloop()
