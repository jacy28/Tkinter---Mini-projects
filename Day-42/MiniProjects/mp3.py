# 🔷 3. Task Manager
# Widgets Used: Listbox, Scrollbar, Entry, Button
# Requirements:
# •	Add tasks into Listbox via Entry field.
# •	Remove selected tasks.
# •	Display 10+ tasks and manage with scrollbar.
# •	Save and load task list from a file.
# •	Double-click on a task to mark it as completed (toggle line-through effect).

import tkinter as tk
from tkinter import messagebox
import os

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
    selected = listbox.curselection()
    for i in reversed(selected):
        listbox.delete(i)

def save_tasks():
    with open("tasks.txt", "w") as f:
        for i in range(listbox.size()):
            task = listbox.get(i)
            f.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def load_tasks():
    if os.path.exists("tasks.txt"):
        listbox.delete(0, tk.END)
        with open("tasks.txt", "r") as f:
            for line in f:
                listbox.insert(tk.END, line.strip())

def toggle_done(event):
    index = listbox.curselection()
    if index:
        i = index[0]
        task = listbox.get(i)
        if task.startswith("✔ "):
            task = task[2:]  # Unmark
        else:
            task = "✔ " + task  # Mark complete
        listbox.delete(i)
        listbox.insert(i, task)

# Main window
root = tk.Tk()
root.title("🔷 Task Manager")
root.geometry("400x400")

# Entry and add button
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=30)
entry.pack(side=tk.LEFT, padx=5)
tk.Button(entry_frame, text="Add Task", command=add_task).pack(side=tk.LEFT)

# Listbox with scrollbar
list_frame = tk.Frame(root)
list_frame.pack()

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(list_frame, width=45, height=12, yscrollcommand=scrollbar.set)
listbox.pack()
scrollbar.config(command=listbox.yview)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Remove Task", command=remove_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Save Tasks", command=save_tasks).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Load Tasks", command=load_tasks).pack(side=tk.LEFT, padx=5)

# Bind double-click to toggle completed
listbox.bind("<Double-Button-1>", toggle_done)

root.mainloop()
