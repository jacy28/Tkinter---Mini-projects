# 42. CPU and RAM Usage Tracker
# •	Show real-time CPU and memory usage
# •	Bar/line chart visualization
# •	Use psutil for stats
# •	Update using after()
# •	Log usage per minute

import tkinter as tk
from tkinter import ttk
import psutil
import time
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LOG_INTERVAL = 60  # seconds
HISTORY_LENGTH = 60  # seconds to keep in chart

cpu_history = []
ram_history = []
timestamps = []

def get_usage():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    return cpu, ram

def update_usage():
    cpu, ram = get_usage()
    cpu_label.config(text=f"CPU Usage: {cpu:.1f}%")
    ram_label.config(text=f"RAM Usage: {ram:.1f}%")

    # Save history
    now = time.strftime("%H:%M:%S")
    cpu_history.append(cpu)
    ram_history.append(ram)
    timestamps.append(now)

    if len(cpu_history) > HISTORY_LENGTH:
        cpu_history.pop(0)
        ram_history.pop(0)
        timestamps.pop(0)

    update_chart()
    log_usage(cpu, ram)
    root.after(1000, update_usage)

def update_chart():
    ax.clear()
    ax.plot(timestamps, cpu_history, label='CPU %', color='blue')
    ax.plot(timestamps, ram_history, label='RAM %', color='green')
    ax.set_ylim(0, 100)
    ax.set_ylabel('% Usage')
    ax.set_xlabel('Time')
    ax.legend()
    ax.set_title("CPU and RAM Usage")
    fig.autofmt_xdate(rotation=45)
    canvas.draw()

def log_usage(cpu, ram):
    current_time = time.time()
    if int(current_time) % LOG_INTERVAL < 2:  # log near each minute
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("usage_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, f"{cpu:.1f}", f"{ram:.1f}"])

# GUI Setup
root = tk.Tk()
root.title("CPU and RAM Usage Tracker")
root.geometry("800x500")

cpu_label = ttk.Label(root, text="CPU Usage: ", font=("Arial", 14))
cpu_label.pack(pady=10)

ram_label = ttk.Label(root, text="RAM Usage: ", font=("Arial", 14))
ram_label.pack(pady=5)

# Chart
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Start tracking
update_usage()
root.mainloop()
