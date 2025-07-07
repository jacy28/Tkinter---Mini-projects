# ✅ 14. Student Attendance Marker
# Scenario: Mark students as present/absent from list.
# Features:
# •	Use Listbox with student names.
# •	Buttons for "Mark Present"/"Absent".
# •	Update color or prefix.
# •	Scrollbar for large list.

import tkinter as tk

def mark_present():
    selected = student_listbox.curselection()
    for i in selected:
        name = student_listbox.get(i)
        if not name.startswith("✓"):
            student_listbox.delete(i)
            student_listbox.insert(i, "✓ " + name.lstrip("✗✓ "))

def mark_absent():
    selected = student_listbox.curselection()
    for i in selected:
        name = student_listbox.get(i)
        if not name.startswith("✗"):
            student_listbox.delete(i)
            student_listbox.insert(i, "✗ " + name.lstrip("✓✗ "))

root = tk.Tk()
root.title("Student Attendance Marker")
root.geometry("400x300")

students = ["Alice", "Bob", "Charlie", "David", "Emma", "Fiona", "George", "Hannah", "Ian", "Julia"]

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

student_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=12, yscrollcommand=scrollbar.set)
for name in students:
    student_listbox.insert(tk.END, name)
student_listbox.pack(padx=10, pady=10)
scrollbar.config(command=student_listbox.yview)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Mark Present", command=mark_present).pack(side="left", padx=10)
tk.Button(btn_frame, text="Mark Absent", command=mark_absent).pack(side="left", padx=10)

root.mainloop()
