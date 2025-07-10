# ✅ 7. Real-Time Entry Validator
# Objective: Enable Submit button only when a valid email is entered.
# Features:
# •	Entry widget for email input.
# •	Bind <KeyRelease> to validate using regex.
# •	If valid → Button becomes normal, else stays disabled.

import tkinter as tk
import re

def validate_email(event=None):
    email = email_entry.get()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

root = tk.Tk()
root.geometry("300x150")

tk.Label(root, text="Enter your email:").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)
email_entry.bind("<KeyRelease>", validate_email)

submit_btn = tk.Button(root, text="Submit", state="disabled")
submit_btn.pack(pady=10)

root.mainloop()
