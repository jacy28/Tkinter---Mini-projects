# ✅ 1. User Registration & Login System
# Scenario: Design a GUI app for user registration and login validation.
# Features:
# •	Entry widgets for username, email, password.
# •	Email validation using regex.
# •	Password masking (show="*").
# •	Button to submit and check credentials.
# •	Dynamic status message using Label.
# •	Frame + grid() layout.

import tkinter as tk
import re

def register_student():
    username= username_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    valid_email=re.match(email_pattern, email)

    if not username or not email or not password:
        message_label.config(text="All fields required.", fg="red")
    elif not valid_email:
        message_label.config(text="Invalid email. Please enter valid email.", fg="red")
    else:
        message_label.config(text="Register Successfully.", fg="green")

root=tk.Tk()
root.title("Registration Form")
root.geometry("400x500")

frame=tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=20)

username_label=tk.Label(frame, text="User Name:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
username_entry=tk.Entry(frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

email_label=tk.Label(frame, text="Email:")
email_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
email_entry=tk.Entry(frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

password_label=tk.Label(frame, text="Password:")
password_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
password_entry=tk.Entry(frame, show="*")
password_entry.grid(row=2, column=1, padx=5, pady=5)

submit_btn=tk.Button(frame, text="Submit", width=10, command=register_student)
submit_btn.grid(row=3, column=1, padx=5, pady=10)

message_label=tk.Label(frame, text="", fg="green")
message_label.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
