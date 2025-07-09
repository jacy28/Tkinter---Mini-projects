# ✅ 14. Form Validation App
# Objective: Build a form with input validation and error dialogs.
# Requirements:
# •	Frame with Entry widgets: Name, Email, Phone.
# •	Submit button validates input.
# •	Show invalid format using messagebox.showerror().
# •	Menu: Form > Reset, Exit.

import tkinter as tk
from tkinter import messagebox
import re

def validate_form():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not email or not phone:
        messagebox.showerror("Validation Error", "All fields are required.")
        return

    if not re.match(r"^[A-Za-z ]+$", name):
        messagebox.showerror("Validation Error", "Name must contain only letters and spaces.")
        return

    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        messagebox.showerror("Validation Error", "Invalid email format.")
        return

    if not re.match(r"^\d{10}$", phone):
        messagebox.showerror("Validation Error", "Phone must be 10 digits.")
        return

    messagebox.showinfo("Success", "Form submitted successfully.")

def reset_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Form Validation App")
root.geometry("400x250")

# Menu
menubar = tk.Menu(root)
form_menu = tk.Menu(menubar, tearoff=0)
form_menu.add_command(label="Reset", command=reset_form)
form_menu.add_separator()
form_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Form", menu=form_menu)
root.config(menu=menubar)

# Form frame
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(fill="both", expand=True)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(form_frame)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Phone:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
phone_entry = tk.Entry(form_frame)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

submit_btn = tk.Button(root, text="Submit", command=validate_form)
submit_btn.pack(pady=10)

root.mainloop()
