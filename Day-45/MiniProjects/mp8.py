# 🔰 8. Task Timer Tracker (Multithread + SQLite)
# Goal: Track tasks and the time spent on each.
# Requirements:
# •	Start/Stop button per task.
# •	Save task name and time in SQLite.
# •	View summary in Listbox.
# •	Use after() to update running timer.

import tkinter as tk
from tkinter import messagebox
import sqlite3
import time

conn = sqlite3.connect("task_timer.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        duration INTEGER
    )
""")
conn.commit()

running = False
start_time = 0
elapsed_time = 0

def start_timer():
    global running, start_time
    if not task_var.get().strip():
        messagebox.showwarning("Missing", "Enter a task name.")
        return
    if not running:
        start_time = time.time()
        running = True
        update_timer()

def stop_timer():
    global running, elapsed_time
    if running:
        running = False
        elapsed = int(time.time() - start_time)
        elapsed_time_label.config(text="00:00:00")
        save_task(task_var.get(), elapsed)
        refresh_tasks()

def update_timer():
    if running:
        now = int(time.time() - start_time)
        h = now // 3600
        m = (now % 3600) // 60
        s = now % 60
        elapsed_time_label.config(text=f"{h:02}:{m:02}:{s:02}")
        root.after(1000, update_timer)

def save_task(name, duration):
    cur.execute("INSERT INTO tasks (name, duration) VALUES (?, ?)", (name, duration))
    conn.commit()

def refresh_tasks():
    listbox.delete(0, tk.END)
    rows = cur.execute("SELECT name, duration FROM tasks").fetchall()
    for name, dur in rows:
        h = dur // 3600
        m = (dur % 3600) // 60
        s = dur % 60
        listbox.insert(tk.END, f"{name} - {h:02}:{m:02}:{s:02}")

root = tk.Tk()
root.title("Task Timer Tracker")
root.geometry("400x450")

task_var = tk.StringVar()

tk.Label(root, text="Task Name").pack(pady=(10, 0))
tk.Entry(root, textvariable=task_var).pack(pady=5)

tk.Button(root, text="Start", command=start_timer).pack(pady=5)
tk.Button(root, text="Stop", command=stop_timer).pack(pady=5)

elapsed_time_label = tk.Label(root, text="00:00:00", font=("Courier", 24))
elapsed_time_label.pack(pady=10)

tk.Label(root, text="Task Summary").pack(pady=(10, 0))
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=5, fill="both", expand=True)

refresh_tasks()
root.mainloop()
