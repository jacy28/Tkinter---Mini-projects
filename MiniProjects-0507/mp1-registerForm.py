# 🟢 1. Student Registration System
# Goal: Collect, validate, and display student details.
# Requirements:
# •	Use Entry for name, email, phone.
# •	Validate email format using regex.
# •	Use Spinbox to select age.
# •	Use Combobox for course selection.
# •	Submit button validates and adds to Listbox with Scrollbar.
# •	Organize form in Frame using grid() layout.
# •	Use Label to show confirmation message.

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def is_valid_phone(phone):
    pattern = r"^[6-9]\d{9}$"
    return re.match(pattern, phone)

def register_student():
    confirmation_label.config(text="")  

    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    age = age_spinbox.get()
    course = course_combobox.get()

    if not name or not email or not phone or not age or not course:
        messagebox.showerror("Input Error", "Please fill all fields.")
        return

    if not is_valid_email(email):
        messagebox.showerror("Invalid email", "Please enter valid email.")
        return

    if not is_valid_phone(phone):
        messagebox.showerror("Invalid phone number", "Please enter valid Phone Number.")
        return

    student_info = f"Name: {name} | Email: {email} | Phone: {phone} | Age: {age} | Course: {course}"
    student_listbox.insert(tk.END, student_info)

    # Clear inputs
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    age_spinbox.set(17)
    course_combobox.set('')

    confirmation_label.config(text="Student registered successfully!")

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x500")

frame = tk.Frame(root)
frame.grid(row=0, column=0)

name_label = tk.Label(frame, text="Name:", padx=20, pady=20)
name_label.grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

email_label = tk.Label(frame, text="Email:", padx=20, pady=20)
email_label.grid(row=1, column=0)
email_entry = tk.Entry(frame)
email_entry.grid(row=1, column=1)

phone_label = tk.Label(frame, text="Phone:", padx=20, pady=20)
phone_label.grid(row=2, column=0)
phone_entry = tk.Entry(frame)
phone_entry.grid(row=2, column=1)

age_label = tk.Label(frame, text="Age", padx=20, pady=20)
age_label.grid(row=3, column=0)
age_spinbox = tk.Spinbox(frame, from_=17, to=24, state="readonly")
age_spinbox.grid(row=3, column=1)

course_label = tk.Label(frame, text="Course", padx=20, pady=20)
course_label.grid(row=4, column=0)
course_combobox = ttk.Combobox(frame, values=["Python", "Java", "Web Developer", "UI/UX Designer"], state="readonly")
course_combobox.grid(row=4, column=1)

submit_btn = tk.Button(root, text="Register Here", command=register_student)
submit_btn.grid(row=1, column=0, padx=20)

list_frame = tk.Frame(root)
list_frame.grid(row=2, column=0, pady=20)

scrollbar = tk.Scrollbar(list_frame, orient="vertical")
student_listbox = tk.Listbox(list_frame, width=70, height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=student_listbox.yview)

student_listbox.grid(row=0, column=0, sticky="w")
scrollbar.grid(row=0, column=1, sticky="ns")

confirmation_label = tk.Label(root, text="", fg="green")
confirmation_label.grid(row=3, column=0)

root.mainloop()
