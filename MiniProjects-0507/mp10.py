# 🟢 10. Feedback Collector
# Goal: Collect multi-line feedback and show summary.
# Requirements:
# •	Use Entry for name and email.
# •	Use Text for comments.
# •	Validate email with regex.
# •	Add to Listbox with scroll.
# •	Clear inputs after submission.

import tkinter as tk
import re

root = tk.Tk()
root.title("Feedback Collector")

name=tk.Label(root, text="Name:")
name.grid(row=0, column=0, sticky="e", padx=5, pady=5)
email=tk.Label(root, text="Email:")
email.grid(row=1, column=0, sticky="e", padx=5, pady=5)
comments=tk.Label(root, text="Comments:")
comments.grid(row=2, column=0, sticky="ne", padx=5, pady=5)

name_entry = tk.Entry(root, width=40)
name_entry.grid(row=0, column=1, padx=5, pady=5)

email_entry = tk.Entry(root, width=40)
email_entry.grid(row=1, column=1, padx=5, pady=5)

comments_text = tk.Text(root, width=30, height=5)
comments_text.grid(row=2, column=1, padx=5, pady=5)

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def submit_feedback():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    comments = comments_text.get("1.0", tk.END).strip()
    if not name or not email or not comments:
        status_var.set("All fields required.")
        return
    if not is_valid_email(email):
        status_var.set("Invalid email.")
        return
    feedback = f"{name} ({email}): {comments}"
    feedback_listbox.insert(tk.END, feedback)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    comments_text.delete("1.0", tk.END)
    status_var.set("Feedback submitted.")

submit_btn = tk.Button(root, text="Submit", command=submit_feedback)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

list_frame = tk.Frame(root)
list_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

feedback_listbox = tk.Listbox(list_frame, width=60, height=8)
scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=feedback_listbox.yview)
feedback_listbox.config(yscrollcommand=scrollbar.set)

feedback_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var, fg="blue")
status_label.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()


