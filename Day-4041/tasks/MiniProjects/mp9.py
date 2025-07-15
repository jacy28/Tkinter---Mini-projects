# 📚 9. Student Registration Form
# Goal: Form to collect student info.
# Requirements:
# •	Fields: Name, Age, Email, Course.
# •	Validate all fields before saving.
# •	Show summary after submission.
# •	Use grid() for structured layout.
# •	Save data to a text file.

import tkinter as tk
from tkinter import messagebox
import re

# --- Validation helpers ---
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email)

def submit_form():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    email = email_entry.get().strip()
    course = course_entry.get().strip()

    # --- Validations ---
    if not name or not age or not email or not course:
        messagebox.showerror("Validation Error", "All fields are required.")
        return
    if not age.isdigit():
        messagebox.showerror("Validation Error", "Age must be a number.")
        return
    if not is_valid_email(email):
        messagebox.showerror("Validation Error", "Enter a valid email.")
        return

    # --- Save to file ---
    with open("students.txt", "a") as file:
        file.write(f"{name}, {age}, {email}, {course}\n")

    # --- Show summary ---
    summary = f"Student Registered:\nName: {name}\nAge: {age}\nEmail: {email}\nCourse: {course}"
    messagebox.showinfo("Success", summary)

    # --- Clear entries ---
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("📚 Student Registration Form")
root.geometry("400x300")

# --- Labels and Entries ---
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=10)

tk.Label(root, text="Course:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
course_entry = tk.Entry(root)
course_entry.grid(row=3, column=1, padx=10)

# --- Submit Button ---
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()
