# ✅ 7. Daily Task List Manager
# Scenario: Create a task manager with input, delete, and scroll.
# Features:
# •	Entry to input task.
# •	Add to Listbox.
# •	Use Scrollbar for long task lists.
# •	Double-click to mark as completed (prefix ✓).

import tkinter as tk

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected = task_listbox.curselection()
    for i in reversed(selected):
        task_listbox.delete(i)

def mark_completed(event):
    index = task_listbox.curselection()
    if index:
        i = index[0]
        text = task_listbox.get(i)
        if not text.startswith("✓"):
            task_listbox.delete(i)
            task_listbox.insert(i, "✓ " + text)

root = tk.Tk()
root.title("Daily Task List Manager")
root.geometry("400x400")

tk.Label(root, text="Enter Task:").pack(anchor="w", padx=10, pady=(10, 0))
task_entry = tk.Entry(root, width=40)
task_entry.pack(padx=10, pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Add Task", command=add_task).pack(side="left", padx=5)
tk.Button(btn_frame, text="Delete Task", command=delete_task).pack(side="left", padx=5)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

task_listbox = tk.Listbox(root, width=50, height=15, yscrollcommand=scrollbar.set)
task_listbox.pack(padx=10, pady=10)
scrollbar.config(command=task_listbox.yview)

task_listbox.bind("<Double-Button-1>", mark_completed)

root.mainloop()
