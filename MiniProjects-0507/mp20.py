# 🟢 20. Attendance Tracker
# Goal: Mark present/absent from a list.
# Requirements:
# •	Use Listbox with student names.
# •	Buttons to mark present or absent.
# •	Color-code present (green) and absent (red).
# •	Use scrollbar for large student list.
# •	Summary shown via Label.

import tkinter as tk

def mark_present():
    selected = student_listbox.curselection()
    for i in selected:
        student_listbox.itemconfig(i, {'bg': 'lightgreen'})
        attendance_status[i] = "Present"
    update_summary()

def mark_absent():
    selected = student_listbox.curselection()
    for i in selected:
        student_listbox.itemconfig(i, {'bg': 'lightcoral'})
        attendance_status[i] = "Absent"
    update_summary()

def update_summary():
    present = sum(1 for status in attendance_status.values() if status == "Present")
    absent = sum(1 for status in attendance_status.values() if status == "Absent")
    summary_label.config(text=f"Present: {present} | Absent: {absent}")

root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("420x480")

students = [f"Student {i+1}" for i in range(40)]
attendance_status = {i: None for i in range(len(students))}

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

scrollbar = tk.Scrollbar(list_frame, orient="vertical")
student_listbox = tk.Listbox(
    list_frame, width=30, height=15,
    yscrollcommand=scrollbar.set, selectmode=tk.MULTIPLE
)
scrollbar.config(command=student_listbox.yview)

student_listbox.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")

for student in students:
    student_listbox.insert(tk.END, student)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

present_button = tk.Button(button_frame, text="Mark Present", bg="lightgreen", command=mark_present)
present_button.grid(row=0, column=0, padx=10)

absent_button = tk.Button(button_frame, text="Mark Absent", bg="lightcoral", command=mark_absent)
absent_button.grid(row=0, column=1, padx=10)

summary_label = tk.Label(root, text="Present: 0 | Absent: 0", font=("Arial", 12))
summary_label.pack(pady=10)

legend_frame = tk.Frame(root)
legend_frame.pack(pady=5)

tk.Label(legend_frame, text="Legend:", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10)
tk.Label(legend_frame, text="Present", bg="lightgreen", width=10).grid(row=0, column=1, padx=5)
tk.Label(legend_frame, text="Absent", bg="lightcoral", width=10).grid(row=0, column=2, padx=5)

root.mainloop()
