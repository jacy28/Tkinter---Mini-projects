# ✅ 13. Employee Shift Scheduler
# Objective: Schedule employees for shifts.
# Requirements:
# •	Frame 1: employee list, Frame 2: shift assignment controls.
# •	Menu: File > Export Schedule.
# •	Toolbar: Assign, Clear.
# •	On export, confirm using a built-in dialog.

import tkinter as tk
from tkinter import messagebox, filedialog

employees = ["Alice", "Bob", "Charlie", "David"]
assignments = {}

def assign_shift():
    selected = emp_listbox.curselection()
    shift = shift_var.get()
    if not selected or not shift:
        messagebox.showwarning("Missing", "Select employee and shift.")
        return
    name = emp_listbox.get(selected[0])
    assignments[name] = shift
    update_assignments()

def clear_assignments():
    assignments.clear()
    update_assignments()

def update_assignments():
    output.delete(0, tk.END)
    for emp, shift in assignments.items():
        output.insert(tk.END, f"{emp}: {shift}")

def export_schedule():
    if not assignments:
        messagebox.showinfo("No Data", "No shifts to export.")
        return
    if not messagebox.askokcancel("Export", "Export current schedule?"):
        return
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w") as f:
            for emp, shift in assignments.items():
                f.write(f"{emp}: {shift}\n")
        messagebox.showinfo("Exported", "Schedule exported successfully.")

root = tk.Tk()
root.title("Employee Shift Scheduler")
root.geometry("500x400")

# Menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Export Schedule", command=export_schedule)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root, bg="#ddd")
toolbar.pack(fill="x")
tk.Button(toolbar, text="Assign", command=assign_shift).pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Clear", command=clear_assignments).pack(side="left", padx=5, pady=5)

# Main layout frames
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

frame1 = tk.Frame(main_frame)
frame1.pack(side="left", fill="y", padx=10)
tk.Label(frame1, text="Employees").pack()
emp_listbox = tk.Listbox(frame1, height=10)
for emp in employees:
    emp_listbox.insert(tk.END, emp)
emp_listbox.pack()

frame2 = tk.Frame(main_frame)
frame2.pack(side="left", fill="both", expand=True)

tk.Label(frame2, text="Select Shift:").pack(pady=5)
shift_var = tk.StringVar()
shifts = ["Morning", "Afternoon", "Night"]
for s in shifts:
    tk.Radiobutton(frame2, text=s, variable=shift_var, value=s).pack(anchor="w")

tk.Label(frame2, text="Assignments:").pack(pady=10)
output = tk.Listbox(frame2, height=10)
output.pack(fill="both", expand=True)

root.mainloop()
