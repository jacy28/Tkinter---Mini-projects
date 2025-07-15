# 📋 4. Contact Form with Validation
# Goal: Allow users to enter contact information and submit it.
# Requirements:
# •	Fields: Name, Email, Message (Text).
# •	Validate name (non-empty), email (regex), and message (min length).
# •	Use grid() layout.
# •	Show “Thank you” message on submit.
# •	Use Label to show validation errors.

import tkinter as tk
import re

# --- Validation Helpers ---
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_and_submit():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    message = message_text.get("1.0", tk.END).strip()

    # Clear previous message
    status_label.config(text="", fg="red")

    if not name:
        status_label.config(text="Name is required.")
    elif not is_valid_email(email):
        status_label.config(text="Invalid email address.")
    elif len(message) < 10:
        status_label.config(text="Message must be at least 10 characters.")
    else:
        status_label.config(text="Thank you for contacting us!", fg="green")

        # Clear the fields
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        message_text.delete("1.0", tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("📋 Contact Form")
root.geometry("400x300")

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, pady=5)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=1, column=1, pady=5)

# Message
tk.Label(root, text="Message:").grid(row=2, column=0, padx=10, pady=5, sticky="ne")
message_text = tk.Text(root, width=30, height=5)
message_text.grid(row=2, column=1, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=validate_and_submit)
submit_btn.grid(row=3, column=1, pady=10)

# Status Label
status_label = tk.Label(root, text="", fg="red")
status_label.grid(row=4, column=1, pady=10)

root.mainloop()
