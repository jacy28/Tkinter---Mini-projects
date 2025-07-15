# 📧 10. Email Validator Tool
# Goal: Check if email input is valid.
# Requirements:
# •	Use Entry for email.
# •	Validate using regex.
# •	Show result in a Label.
# •	Layout with pack().
# •	Add Clear button to reset field.

import tkinter as tk
import re

# --- Email validation function ---
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email)

# --- Validate button action ---
def validate_email():
    email = email_entry.get().strip()
    if is_valid_email(email):
        result_label.config(text="✅ Valid Email", fg="green")
    else:
        result_label.config(text="❌ Invalid Email", fg="red")

# --- Clear input and result ---
def clear_fields():
    email_entry.delete(0, tk.END)
    result_label.config(text="")

# --- GUI Setup ---
root = tk.Tk()
root.title("📧 Email Validator")
root.geometry("300x180")

tk.Label(root, text="Enter Email:", font=("Arial", 12)).pack(pady=10)
email_entry = tk.Entry(root, font=("Arial", 12), width=30)
email_entry.pack()

validate_btn = tk.Button(root, text="Validate", command=validate_email)
validate_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear", command=clear_fields)
clear_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
