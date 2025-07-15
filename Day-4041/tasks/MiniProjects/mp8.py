# 📅 8. To-Do List App
# Goal: Add, view, and delete tasks.
# Requirements:
# •	Use Entry for task input.
# •	Text or Listbox to show tasks.
# •	Buttons: Add Task, Delete Task, Clear All.
# •	Use pack() layout.
# •	Optional: Save tasks to file.

import tkinter as tk
from tkinter import messagebox
import os

# --- File to store tasks ---
TASK_FILE = "tasks.txt"

# --- Add Task ---
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# --- Delete Selected Task ---
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Select Task", "Please select a task to delete.")

# --- Clear All Tasks ---
def clear_tasks():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        task_listbox.delete(0, tk.END)

# --- Save tasks to file ---
def save_tasks():
    with open(TASK_FILE, "w") as f:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            f.write(task + "\n")

# --- Load tasks from file ---
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())

# --- GUI Setup ---
root = tk.Tk()
root.title("📅 To-Do List")
root.geometry("400x400")

tk.Label(root, text="Enter a task:", font=("Arial", 12)).pack(pady=10)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

tk.Button(root, text="Add Task", command=add_task).pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

tk.Button(root, text="Delete Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Clear All", command=clear_tasks).pack(pady=5)

# Load saved tasks
load_tasks()

# Save tasks on close
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))

root.mainloop()
