# 18. Employee Shift Scheduler
# Objective: Assign and display employee shifts.
# Features:
# •	Use Entry for employee name.
# •	Combobox to choose shift type.
# •	Spinbox for number of working hours.
# •	Add to Listbox with scrollbar.
# •	Layout with grid() in Frames.


import tkinter as tk
from tkinter import ttk

def add_shift():
    name = name_entry.get().strip()
    shift = shift_combo.get()
    hours = hours_spinbox.get()

    if not name or not shift or not hours:
        return

    entry = f"{name} - {shift} - {hours} hrs"
    shift_listbox.insert(tk.END, entry)

    name_entry.delete(0, tk.END)
    shift_combo.set('')
    hours_spinbox.delete(0, tk.END)
    hours_spinbox.insert(0, "1")

root = tk.Tk()
root.title("Employee Shift Scheduler")
root.geometry("400x350")

# Input Frame
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(input_frame, text="Employee Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Shift Type:").grid(row=1, column=0, sticky="w", pady=5)
shift_combo = ttk.Combobox(input_frame, values=["Morning", "Afternoon", "Night"], state="readonly")
shift_combo.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Working Hours:").grid(row=2, column=0, sticky="w", pady=5)
hours_spinbox = tk.Spinbox(input_frame, from_=4, to=12)
hours_spinbox.grid(row=2, column=1, pady=5)

add_button = tk.Button(input_frame, text="Add Shift", command=add_shift)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Listbox Frame
list_frame = tk.Frame(root)
list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

shift_listbox = tk.Listbox(list_frame, height=10, width=40)
shift_listbox.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=shift_listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

shift_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
