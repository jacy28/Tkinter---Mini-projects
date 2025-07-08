# 5.	To-Do List App
# 	Entry for task, Button to add task, Listbox or Label to show current tasks, and Button to remove selected/completed tasks.

import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a task.")
    else:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No task selected.")
    else:
        for i in selected[::-1]:  # Reverse to avoid index shift
            task_listbox.delete(i)

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task, width=20, bg="lightgreen")
add_btn.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, width=40, height=10, yscrollcommand=scrollbar.set, selectmode=tk.MULTIPLE)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=task_listbox.yview)

remove_btn = tk.Button(root, text="Remove Selected Task(s)", command=remove_task, width=25, bg="tomato")
remove_btn.pack(pady=10)

root.mainloop()
