# 🔰 3. Background Task Notifier (Multithreading + after())
# Goal: Run background tasks (e.g., simulated download) without freezing GUI.
# Requirements:
# •	Start button starts thread.
# •	Thread simulates task using sleep().
# •	Use after() to update progress label from the thread.
# •	Show completion message in label.

import tkinter as tk
import threading
import time

def start_task():
    threading.Thread(target=run_task, daemon=True).start()

def run_task():
    for i in range(1, 6):
        time.sleep(1)
        update_label(f"Processing... {i}/5")
    update_label("✅ Task Completed!")

def update_label(msg):
    root.after(0, lambda: status_label.config(text=msg))

root = tk.Tk()
root.title("Background Task Notifier")
root.geometry("300x150")

start_button = tk.Button(root, text="Start Task", command=start_task)
start_button.pack(pady=20)

status_label = tk.Label(root, text="Idle")
status_label.pack(pady=10)

root.mainloop()
