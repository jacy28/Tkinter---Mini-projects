# 8. To-Do List Manager
# Objective: Manage daily tasks with scrolling.
# Features:
# •	Use Entry to input task.
# •	Listbox to display tasks.
# •	Add task button.
# •	Scrollbar for 20+ tasks.
# •	Double-click a task to mark as done (e.g., prefix with ✓).
# •	Save/Load list (optional with file).

import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        tasks.append(task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def mark_done(event):
    selection = task_listbox.curselection()
    if selection:
        index = selection[0]
        task = task_listbox.get(index)
        if not task.startswith("✓"):
            task_listbox.delete(index)
            task = "✓ " + task
            task_listbox.insert(index, task)
            tasks[index] = task

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in task_listbox.get(0, tk.END):
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def load_tasks():
    task_listbox.delete(0, tk.END)
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                task = line.strip()
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        messagebox.showwarning("No File", "tasks.txt not found.")

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

frame = tk.Frame(root)
frame.pack(pady=10, fill="both", expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

task_listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=15, selectbackground="lightgray")
task_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=task_listbox.yview)

task_listbox.bind("<Double-Button-1>", mark_done)


bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

save_btn = tk.Button(bottom_frame, text="Save", command=save_tasks)
save_btn.pack(side="left", padx=10)

load_btn = tk.Button(bottom_frame, text="Load", command=load_tasks)
load_btn.pack(side="left", padx=10)


root.mainloop()
