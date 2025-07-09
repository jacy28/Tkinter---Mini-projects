# ✅ 11. To-Do List Manager with Dialogs
# Objective: Manage tasks with custom input dialogs.
# Requirements:
# •	Use PanedWindow (vertical) to split input area and task display.
# •	Toolbar: Add Task, Delete Task.
# •	On Add, open a custom Toplevel() to enter task name, deadline.
# •	Menu bar for File > Save List, Exit.

import tkinter as tk
from tkinter import messagebox, filedialog

tasks = []

def add_task_dialog():
    dialog = tk.Toplevel(root)
    dialog.title("Add Task")
    dialog.geometry("300x150")
    dialog.grab_set()

    tk.Label(dialog, text="Task Name:").grid(row=0, column=0, padx=10, pady=5)
    task_entry = tk.Entry(dialog)
    task_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(dialog, text="Deadline:").grid(row=1, column=0, padx=10, pady=5)
    deadline_entry = tk.Entry(dialog)
    deadline_entry.grid(row=1, column=1, padx=10, pady=5)

    def submit_task():
        task = task_entry.get()
        deadline = deadline_entry.get()
        if task:
            item = f"{task} - Due: {deadline if deadline else 'N/A'}"
            task_listbox.insert(tk.END, item)
            tasks.append(item)
            dialog.destroy()
        else:
            messagebox.showwarning("Missing", "Task name is required.")

    tk.Button(dialog, text="Submit", command=submit_task).grid(row=2, column=0, columnspan=2, pady=10)

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task_listbox.delete(index)
        del tasks[index]
    else:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

def save_tasks():
    if not tasks:
        messagebox.showinfo("Empty List", "No tasks to save.")
        return
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully.")

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

# Menu bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Save List", command=save_tasks)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root, bg="#eee")
toolbar.pack(fill="x")
tk.Button(toolbar, text="Add Task", command=add_task_dialog).pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Delete Task", command=delete_task).pack(side="left", padx=5, pady=5)

# PanedWindow
paned = tk.PanedWindow(root, orient=tk.VERTICAL)
paned.pack(fill="both", expand=True)

# Task display listbox
task_frame = tk.Frame(paned)
task_listbox = tk.Listbox(task_frame)
task_listbox.pack(fill="both", expand=True, padx=10, pady=10)
paned.add(task_frame)

root.mainloop()
