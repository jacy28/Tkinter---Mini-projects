# ✅ 8. Email Validator Utility
# Scenario: GUI app to check valid email using regex.
# Features:
# •	Entry for email.
# •	Button to validate.
# •	Show result dynamically in Label.
# •	Change label color (green/red) based on result.

import tkinter as tk
import re

def validate_email():
    email = email_entry.get()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        result_label.config(text="Valid Email", fg="green")
    else:
        result_label.config(text="Invalid Email", fg="red")

root = tk.Tk()
root.title("Email Validator")
root.geometry("350x200")

email_label=tk.Label(root, text="Enter Email:")
email_label.pack(pady=(20, 5))
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)

tk.Button(root, text="Validate", command=validate_email).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
