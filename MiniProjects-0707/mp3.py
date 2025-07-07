# ✅ 3. Feedback Collector with Scrollable View
# Scenario: Collect user feedback and display it in a scrollable list.
# Features:
# •	Entry for name, Text for comments.
# •	Email format validation.
# •	Use Listbox with Scrollbar to show feedbacks.
# •	Button to add and clear feedback.

import tkinter as tk
from tkinter import messagebox
import re

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def add_feedback():
    name=name_entry.get()
    email=email_entry.get()
    comments=comments_text.get("1.0", tk.END).strip()

    if not name or not email or not comments:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return
    
    if not valid_email(email):
        messagebox.showerror("Invalid email", "Please enter valid email.")
        return
    
    feedback=f"Name: {name}, Email: {email}, Comments: {comments}"
    listbox.insert(tk.END, feedback)

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    comments_text.delete("1.0", tk.END)
    
def clear_feedback():
    listbox.delete(0, tk.END)

root=tk.Tk()
root.title("Feedback Collector")
root.geometry("400x400")

name_label = tk.Label(root, text="Name:")
name_label.pack(anchor="w", padx=10)
name_entry = tk.Entry(root)
name_entry.pack(padx=10)

email_label = tk.Label(root, text="Email:")
email_label.pack(anchor="w", padx=10, pady=(10, 0))
email_entry = tk.Entry(root)
email_entry.pack(padx=10)

comments_label = tk.Label(root, text="Comments:")
comments_label.pack(anchor="w", padx=10, pady=(10, 0))
comments_text = tk.Text(root, width=50, height=4)
comments_text.pack(padx=10)

add_btn=tk.Button(root, text="Add Feedback", command=add_feedback)
add_btn.pack(padx=10)
clear_btn=tk.Button(root, text="Clear Feedback", command=clear_feedback)
clear_btn.pack(padx=10)

scrollbar=tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

listbox=tk.Listbox(root, yscrollcommand=scrollbar.set, width=80, height=10)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)

root.mainloop()