# 🔰 16. Custom Download Simulation Tool (Thread + Progress)
# Goal: Simulate file download with progress bar.
# Requirements:
# •	Use Thread to fake download.
# •	Progress bar updates using after().
# •	Start/Cancel buttons.

import tkinter as tk
from tkinter import ttk
import threading
import time

running = False
progress_value = 0

def start_download():
    global running, progress_value
    if not running:
        running = True
        progress_value = 0
        progress_bar["value"] = 0
        threading.Thread(target=simulate_download, daemon=True).start()

def cancel_download():
    global running
    running = False

def simulate_download():
    global progress_value
    while running and progress_value < 100:
        time.sleep(0.1)
        progress_value += 1
        root.after(0, update_progress)
    if progress_value >= 100:
        root.after(0, lambda: status_label.config(text="Download Complete"))

def update_progress():
    progress_bar["value"] = progress_value
    status_label.config(text=f"Progress: {progress_value}%")

root = tk.Tk()
root.title("Download Simulation Tool")
root.geometry("400x200")

progress_bar = ttk.Progressbar(root, length=300, mode="determinate", maximum=100)
progress_bar.pack(pady=30)

tk.Button(root, text="Start Download", command=start_download).pack(pady=5)
tk.Button(root, text="Cancel", command=cancel_download).pack(pady=5)

status_label = tk.Label(root, text="Progress: 0%")
status_label.pack(pady=10)

root.mainloop()
