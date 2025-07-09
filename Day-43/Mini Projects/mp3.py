# ✅ 3. Multi-Section Registration Form
# Objective: Collect user details in categorized sections.
# Requirements:
# •	Use Frames for: Personal Info, Contact Info, Account Info.
# •	Add Label, Entry, Spinbox, Combobox widgets inside each frame.
# •	Submit button shows a summary in a new Toplevel() window (custom dialog).
# •	Use grid() layout inside each frame for neat organization.

import tkinter as tk
from tkinter import ttk, Toplevel

def submit_form():
    summary = (
        f"Name: {name_entry.get()}\n"
        f"Age: {age_spinbox.get()}\n"
        f"Gender: {gender_combo.get()}\n"
        f"Email: {email_entry.get()}\n"
        f"Phone: {phone_entry.get()}\n"
        f"Username: {username_entry.get()}\n"
        f"Password: {password_entry.get()}"
    )
    
    top = Toplevel(root)
    top.title("Submission Summary")
    top.geometry("300x250")
    tk.Label(top, text="Submitted Information:", font=('Arial', 12, 'bold')).pack(pady=10)
    tk.Label(top, text=summary, justify="left").pack(padx=10)

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x500")

# Personal Info Frame
personal_frame = tk.LabelFrame(root, text="Personal Info", padx=10, pady=10)
personal_frame.pack(padx=10, pady=10, fill="x")

tk.Label(personal_frame, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(personal_frame)
name_entry.grid(row=0, column=1)

tk.Label(personal_frame, text="Age:").grid(row=1, column=0, sticky="w")
age_spinbox = tk.Spinbox(personal_frame, from_=0, to=120)
age_spinbox.grid(row=1, column=1)

tk.Label(personal_frame, text="Gender:").grid(row=2, column=0, sticky="w")
gender_combo = ttk.Combobox(personal_frame, values=["Male", "Female", "Other"], state="readonly")
gender_combo.grid(row=2, column=1)

# Contact Info Frame
contact_frame = tk.LabelFrame(root, text="Contact Info", padx=10, pady=10)
contact_frame.pack(padx=10, pady=10, fill="x")

tk.Label(contact_frame, text="Email:").grid(row=0, column=0, sticky="w")
email_entry = tk.Entry(contact_frame)
email_entry.grid(row=0, column=1)

tk.Label(contact_frame, text="Phone:").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(contact_frame)
phone_entry.grid(row=1, column=1)

# Account Info Frame
account_frame = tk.LabelFrame(root, text="Account Info", padx=10, pady=10)
account_frame.pack(padx=10, pady=10, fill="x")

tk.Label(account_frame, text="Username:").grid(row=0, column=0, sticky="w")
username_entry = tk.Entry(account_frame)
username_entry.grid(row=0, column=1)

tk.Label(account_frame, text="Password:").grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(account_frame, show="*")
password_entry.grid(row=1, column=1)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.pack(pady=20)

root.mainloop()
