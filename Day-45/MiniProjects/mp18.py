# 🔰 18. System Info Viewer (Thread + Label)
# Goal: Display live CPU usage or time.
# Requirements:
# •	Background thread collects info.
# •	Update GUI every 1 second.
# •	Safe update using after().

import tkinter as tk
import threading
import time
import psutil
from datetime import datetime

def start_updater():
    threading.Thread(target=fetch_info, daemon=True).start()

def fetch_info():
    while True:
        time.sleep(1)
        cpu = psutil.cpu_percent()
        now = datetime.now().strftime("%H:%M:%S")
        root.after(0, lambda: label.config(text=f"Time: {now}\nCPU: {cpu}%"))

root = tk.Tk()
root.title("System Info Viewer")
root.geometry("300x150")

label = tk.Label(root, text="Fetching...", font=("Arial", 14), justify="center")
label.pack(expand=True)

start_updater()
root.mainloop()
