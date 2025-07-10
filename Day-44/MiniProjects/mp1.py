# ✅ 1. Login Form with Dynamic Button State
# Objective: Enable the “Login” button only when both username and password fields are filled.
# Features:
# •	Entry widgets for username and password.
# •	Button with state='disabled' initially.
# •	Use <KeyRelease> to monitor inputs and enable button when both fields are non-empty.
# •	Password field masked using show="*".

import tkinter as tk
root=tk.Tk()
root.geometry("300x300")
def check_fields(event):
    username=name_entry.get()
    password=pw_entry.get()
    if username and password:
        btn.config(state="normal")
    else:
        btn.config(state="disabled")
def login():
    print("Login Successfully.")
name_label=tk.Label(root, text="User Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry=tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)
pw_label=tk.Label(root, text="Password:")
pw_label.grid(row=1, column=0, padx=5, pady=5)
pw_entry=tk.Entry(root, show="*")
pw_entry.grid(row=1, column=1, padx=5, pady=5)
name_entry.bind("<KeyRelease>", check_fields)
pw_entry.bind("<KeyRelease>", check_fields)
btn=tk.Button(root, text="Login", command=login, state="disabled")
btn.grid(row=2, column=1, padx=5, pady=5)
root.mainloop()