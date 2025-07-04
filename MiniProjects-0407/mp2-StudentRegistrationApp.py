# 2. Student Registration App
# Objective: Register students with input validation and display summary.
# Features:
# •	Entry for Name, Email.
# •	Combobox for selecting Course.
# •	Spinbox for Age.
# •	Listbox to show all registered students.
# •	Button to submit data.
# •	Scrollbar for long student list.
# •	Layout managed with pack() inside Frames.

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


def register_student():
    name = name_entry.get()
    email = email_entry.get()
    course = course_combo.get()
    age = age_spinbox.get()

    if not name or not email or not course:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email.")
        return

    student_info = f"Name: {name}\nEmail: {email}\nCourse: {course}\nAge: {age}"
    student_listbox.insert(tk.END, student_info)

    # Clear inputs
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_combo.set('')
    age_spinbox.delete(0, tk.END)
    age_spinbox.insert(0, 18)


root = tk.Tk()
root.title("Student Registration App")
root.geometry("500x400")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

name_label=tk.Label(input_frame, text="Name:")
name_label.pack(anchor="w")
name_entry = tk.Entry(input_frame, width=40)
name_entry.pack(pady=2)

email_label=tk.Label(input_frame, text="Email:")
email_label.pack(anchor="w")
email_entry = tk.Entry(input_frame, width=40)
email_entry.pack(pady=2)

course_label=tk.Label(input_frame, text="Course:")
course_label.pack(anchor="w")
course_combo = ttk.Combobox(input_frame, values=["Python", "Java", "C++", "Web Dev"])
course_combo.pack(pady=2)

age_label=tk.Label(input_frame, text="Age:")
age_label.pack(anchor="w")
age_spinbox = tk.Spinbox(input_frame, from_=18, to=60, width=5)
age_spinbox.pack(pady=2)

submit_btn = tk.Button(input_frame, text="Register Student", command=register_student)
submit_btn.pack(pady=10)

list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

student_listbox = tk.Listbox(list_frame, width=60, height=10, yscrollcommand=scrollbar.set)
student_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=student_listbox.yview)


root.mainloop()



