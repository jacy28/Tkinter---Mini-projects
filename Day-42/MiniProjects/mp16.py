# 🔷 16. Employee Shift Scheduler
# Widgets Used: Listbox, Scrollbar, Combobox, Spinbox
# Requirements:
# •	List of employees in Listbox.
# •	Combobox for shift type (Morning, Evening, Night).
# •	Spinbox for hours assigned.
# •	Assign button to allocate shift.
# •	List shifts with scrollbar support.

import tkinter as tk
from tkinter import ttk

# --- Setup main window ---
root = tk.Tk()
root.title("🔷 Employee Shift Scheduler")
root.geometry("600x400")

# --- Sample Employees ---
employees = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen", "Ian", "Julia"]

# --- Frames ---
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# --- Employee Listbox with Scrollbar ---
tk.Label(left_frame, text="Employees").pack()
emp_scroll = tk.Scrollbar(left_frame)
emp_listbox = tk.Listbox(left_frame, height=15, yscrollcommand=emp_scroll.set, selectmode=tk.SINGLE)
emp_scroll.config(command=emp_listbox.yview)
emp_scroll.pack(side=tk.RIGHT, fill=tk.Y)
emp_listbox.pack(side=tk.LEFT)

for emp in employees:
    emp_listbox.insert(tk.END, emp)

# --- Controls for assigning shift ---
controls = tk.Frame(right_frame)
controls.pack(pady=10)

tk.Label(controls, text="Shift Type:").grid(row=0, column=0, padx=5, sticky="e")
shift_combo = ttk.Combobox(controls, values=["Morning", "Evening", "Night"], state="readonly")
shift_combo.grid(row=0, column=1, padx=5)
shift_combo.set("Morning")

tk.Label(controls, text="Hours:").grid(row=0, column=2, padx=5, sticky="e")
hours_spin = tk.Spinbox(controls, from_=1, to=12, width=5)
hours_spin.grid(row=0, column=3, padx=5)

# --- Assigned Shifts Listbox with Scrollbar ---
tk.Label(right_frame, text="Assigned Shifts").pack()
output_scroll = tk.Scrollbar(right_frame)
output_listbox = tk.Listbox(right_frame, height=12, yscrollcommand=output_scroll.set, width=50)
output_scroll.config(command=output_listbox.yview)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# --- Assign Shift Button ---
def assign_shift():
    selected = emp_listbox.curselection()
    if not selected:
        return
    name = emp_listbox.get(selected)
    shift = shift_combo.get()
    hours = hours_spin.get()
    record = f"{name} → {shift} Shift ({hours} hrs)"
    output_listbox.insert(tk.END, record)

btn = tk.Button(right_frame, text="Assign Shift", command=assign_shift)
btn.pack(pady=10)

root.mainloop()
