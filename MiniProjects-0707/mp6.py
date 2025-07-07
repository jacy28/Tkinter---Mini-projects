# ✅ 6. Student Course Enrollment App
# Scenario: GUI to register students for specific courses.
# Features:
# •	Entry for name, email.
# •	Combobox to select course.
# •	Spinbox for age.
# •	Display enrolled students in Listbox with Scrollbar.

import tkinter as tk
from tkinter import ttk, messagebox

def enroll_student():
    name = name_entry.get()
    email = email_entry.get()
    age = age_spinbox.get()
    course = course_combo.get()

    if not name or not email or not course:
        messagebox.showerror("Input Error", "Please fill all required fields.")
        return

    enrolled_student = f"Name: {name}, Email: {email}, Age: {age}, Course: {course}"
    student_listbox.insert(tk.END, enrolled_student)

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    age_spinbox.delete(0, tk.END)
    age_spinbox.insert(0, "18")
    course_combo.set("")

root = tk.Tk()
root.title("Student Course Enrollment")
root.geometry("500x400")

name_label=tk.Label(root, text="Name:")
name_label.pack(anchor="w", padx=10)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=10)

email_label=tk.Label(root, text="Email:")
email_label.pack(anchor="w", padx=10, pady=(10, 0))
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=10)

age_label=tk.Label(root, text="Age:")
age_label.pack(anchor="w", padx=10, pady=(10, 0))
age_spinbox = tk.Spinbox(root, from_=18, to=55, width=5)
age_spinbox.pack(padx=10)
age_spinbox.delete(0, tk.END)
age_spinbox.insert(0, "18")

course_label=tk.Label(root, text="Course:")
course_label.pack(anchor="w", padx=10, pady=(10, 0))
course_combo = ttk.Combobox(root, values=["Python", "Java", "C++", "Web Dev"], state="readonly", width=37)
course_combo.pack(padx=10)

enroll_btn = tk.Button(root, text="Enroll", command=enroll_student)
enroll_btn.pack(pady=10)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

student_listbox = tk.Listbox(root, width=80, height=10, yscrollcommand=scrollbar.set)
student_listbox.pack(padx=10, pady=10)
scrollbar.config(command=student_listbox.yview)

root.mainloop()
