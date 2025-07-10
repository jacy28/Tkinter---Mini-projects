# ✅ 13. Task Manager with Completion Toggle
# Objective: Click to mark a task as complete (color change or prefix ✔).
# Features:
# •	Listbox showing tasks.
# •	On <Double-Button-1> → toggle task to completed.
# •	Use .get() and .delete() + .insert() to update text.

import tkinter as tk

def toggle_task(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        task = listbox.get(index)

        if task.startswith("✔ "):
            task = task[2:]  # remove check mark
        else:
            task = "✔ " + task  # add check mark

        listbox.delete(index)
        listbox.insert(index, task)

root = tk.Tk()
root.geometry("300x250")
root.title("Task Manager")

tasks = ["Buy groceries", "Read a book", "Call Alice", "Finish project"]
listbox = tk.Listbox(root, font=("Arial", 12))
for task in tasks:
    listbox.insert(tk.END, task)
listbox.pack(padx=10, pady=10, fill="both", expand=True)

listbox.bind("<Double-Button-1>", toggle_task)

root.mainloop()
