# ✅ 15. Multi-Frame Form Navigation
# Scenario: Multi-step registration using Frames.
# Features:
# •	Frame 1: Personal Info (Name, Age).
# •	Frame 2: Course & Skill Info (Combobox, Entry).
# •	Frame 3: Submit + Summary.
# •	Navigation buttons between frames.

import tkinter as tk
from tkinter import ttk, messagebox

def show_frame(frame):
    frame.tkraise()

def next_to_frame2():
    if not name_entry.get().strip() or not age_spin.get().strip():
        messagebox.showerror("Error", "Please fill in all personal info.")
        return
    show_frame(frame2)

def next_to_frame3():
    if not course_combo.get() or not skill_entry.get().strip():
        messagebox.showerror("Error", "Please select a course and enter skill.")
        return
    name = name_entry.get()
    age = age_spin.get()
    course = course_combo.get()
    skill = skill_entry.get()
    summary = f"Name: {name}\nAge: {age}\nCourse: {course}\nSkill: {skill}"
    summary_label.config(text=summary)
    show_frame(frame3)

def back_to_frame1():
    show_frame(frame1)

def back_to_frame2():
    show_frame(frame2)

def submit_form():
    data = summary_label.cget("text")
    messagebox.showinfo("Submitted", "Form submitted successfully!")
    with open("registration.txt", "w") as file:
        file.write(data)
    root.quit()

root = tk.Tk()
root.title("Multi-Frame Registration")
root.geometry("400x300")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Frame 1
tk.Label(frame1, text="Personal Information", font=("Arial", 14)).pack(pady=10)
tk.Label(frame1, text="Name:").pack(anchor="w", padx=10)
name_entry = tk.Entry(frame1)
name_entry.pack(padx=10)

tk.Label(frame1, text="Age:").pack(anchor="w", padx=10, pady=(10, 0))
age_spin = tk.Spinbox(frame1, from_=10, to=100)
age_spin.pack(padx=10)

tk.Button(frame1, text="Next", command=next_to_frame2).pack(pady=20)

# Frame 2
tk.Label(frame2, text="Course & Skill Info", font=("Arial", 14)).pack(pady=10)
tk.Label(frame2, text="Course:").pack(anchor="w", padx=10)
course_combo = ttk.Combobox(frame2, values=["Python", "Java", "Web Dev"], state="readonly")
course_combo.pack(padx=10)

tk.Label(frame2, text="Skill Level:").pack(anchor="w", padx=10, pady=(10, 0))
skill_entry = tk.Entry(frame2)
skill_entry.pack(padx=10)

btn_frame2 = tk.Frame(frame2)
btn_frame2.pack(pady=20)
tk.Button(btn_frame2, text="Back", command=back_to_frame1).pack(side="left", padx=10)
tk.Button(btn_frame2, text="Next", command=next_to_frame3).pack(side="left", padx=10)

# Frame 3
tk.Label(frame3, text="Summary", font=("Arial", 14)).pack(pady=10)
summary_label = tk.Label(frame3, text="", justify="left")
summary_label.pack(padx=10, pady=10)

tk.Button(frame3, text="Back", command=back_to_frame2).pack(pady=5)
tk.Button(frame3, text="Submit", command=submit_form).pack(pady=5)

show_frame(frame1)
root.mainloop()
