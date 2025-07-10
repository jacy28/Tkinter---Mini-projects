# 🔰 1. Student Registration System (SQLite + Validation)
# Goal: Register students with name, age, and course, and store it in SQLite.
# Requirements:
# •	Entry fields for Name, Age, Course.
# •	Save button stores data in SQLite.
# •	“View All” shows all records in Listbox.
# •	Validate inputs (age must be numeric).
# •	Use filedialog to export records to .txt.

import sqlite3
import tkinter as tk
from tkinter import messagebox, filedialog

# --- Database Setup ---
conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL
    )
""")
conn.commit()

# --- Functions ---
def validate_inputs(name, age, course):
    if not name or not age or not course:
        messagebox.showwarning("Validation Error", "All fields are required.")
        return False
    if not age.isdigit():
        messagebox.showwarning("Validation Error", "Age must be a number.")
        return False
    return True

def save_student():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    course = course_entry.get().strip()
    if validate_inputs(name, age, course):
        cur.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, int(age), course))
        conn.commit()
        messagebox.showinfo("Success", "Student registered successfully.")
        clear_fields()
        view_all()

def view_all():
    listbox.delete(0, tk.END)
    cur.execute("SELECT name, age, course FROM students")
    for row in cur.fetchall():
        listbox.insert(tk.END, f"Name: {row[0]}, Age: {row[1]}, Course: {row[2]}")

def export_records():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        cur.execute("SELECT name, age, course FROM students")
        with open(file_path, 'w') as f:
            for row in cur.fetchall():
                f.write(f"Name: {row[0]}, Age: {row[1]}, Course: {row[2]}\n")
        messagebox.showinfo("Exported", f"Records exported to {file_path}")

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Student Registration System")
root.geometry("400x500")

# Labels and Entry Fields
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Course:").pack(pady=5)
course_entry = tk.Entry(root)
course_entry.pack()

# Buttons
tk.Button(root, text="Save", command=save_student).pack(pady=10)
tk.Button(root, text="View All", command=view_all).pack(pady=5)
tk.Button(root, text="Export to TXT", command=export_records).pack(pady=5)

# Listbox to display students
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=20)

root.mainloop()
