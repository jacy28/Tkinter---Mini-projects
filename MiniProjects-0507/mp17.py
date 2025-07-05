# 🟢 17. Email Validator App
# Goal: Validate user email input.
# Requirements:
# •	Use Entry for email.
# •	Button checks using regex.
# •	Show validation result using Label.
# •	Change Label color based on valid/invalid.

import tkinter as tk
import re

def validate_email():
    email = email_entry.get()
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    result = re.match(pattern, email)

    if result:
        result_label.config(text="Valid Email", fg="green")
    else:
        result_label.config(text="Invalid Email", fg="red")


root = tk.Tk()
root.title("Email Validator")
root.geometry("400x200")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=30)

email_label = tk.Label(frame, text="Enter Email:")
email_label.grid(row=0, column=0, pady=10)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=0, column=1, pady=10)

validate_button = tk.Button(root, text="Validate", command=validate_email)
validate_button.grid(row=1, column=0, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.grid(row=2, column=0)

root.mainloop()
