# 🟢 8. To-Do List Manager
# Goal: Add, remove, and mark tasks.
# Requirements:
# •	Entry for task input.
# •	Button to add to Listbox.
# •	Use Scrollbar if list >10.
# •	Bind task click to mark it done.
# •	Use .delete(), .insert() to update list.

import tkinter as tk

root = tk.Tk()
root.title("To-Do List Manager")

tk.Label(root, text="New Task:").pack(pady=5)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def mark_done(event):
    selection = task_listbox.curselection()
    if selection:
        index = selection[0]
        task = task_listbox.get(index)
        if not task.startswith("✔ "):
            task_listbox.delete(index)
            task_listbox.insert(index, "✔ " + task)

def remove_task():
    selection = task_listbox.curselection()
    if selection:
        task_listbox.delete(selection[0])

frame = tk.Frame(root)
frame.pack(pady=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

task_listbox = tk.Listbox(list_frame, width=50, height=10)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=task_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)

task_listbox.bind("<Double-Button-1>", mark_done)

root.mainloop()
