# 📑 17. Feedback Collector
# Goal: Users enter name, email, and feedback.
# Requirements:
# •	Use Entry, Text for feedback.
# •	Validate fields.
# •	Show thank-you message on submit.
# •	Store data in a text file.

import tkinter as tk
import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def submit_feedback():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    feedback = feedback_text.get("1.0", tk.END).strip()

    if not name or not email or not feedback:
        status_label.config(text="All fields are required.", fg="red")
        return

    if not is_valid_email(email):
        status_label.config(text="Invalid email format.", fg="red")
        return

    with open("feedback.txt", "a") as f:
        f.write(f"Name: {name}\nEmail: {email}\nFeedback:\n{feedback}\n{'-'*40}\n")

    status_label.config(text="Thank you for your feedback!", fg="green")

    # Clear fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)

# Main window
root = tk.Tk()
root.title("📑 Feedback Collector")
root.geometry("400x400")

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=1, column=1, pady=5)

# Feedback
tk.Label(root, text="Feedback:").grid(row=2, column=0, padx=10, pady=5, sticky="ne")
feedback_text = tk.Text(root, height=8, width=30)
feedback_text.grid(row=2, column=1, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_feedback)
submit_btn.grid(row=3, column=1, pady=10)

# Status/Message Label
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
