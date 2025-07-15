# 43. Battery Health Monitor
# •	Get battery % and status from psutil
# •	Show charge/discharge graph
# •	Alert at low or full charge
# •	Estimated time remaining
# •	Log usage data

import psutil
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import csv
import os

# ------------------- Global Setup ------------------- #
battery_levels = []
timestamps = []
MAX_POINTS = 30
LOG_FILE = f"battery_log_{datetime.now().strftime('%Y-%m-%d')}.csv"

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Battery %", "Charging", "Time Left"])

# ------------------- GUI ------------------- #
root = tk.Tk()
root.title("Battery Health Monitor")
root.geometry("800x500")

status_label = tk.Label(root, text="", font=("Segoe UI", 14))
status_label.pack(pady=10)

time_label = tk.Label(root, text="", font=("Segoe UI", 12))
time_label.pack()

# ------------------- Graph ------------------- #
fig, ax = plt.subplots(figsize=(8, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# ------------------- Update Function ------------------- #
def update_battery():
    battery = psutil.sensors_battery()
    if battery is None:
        status_label.config(text="Battery status not available.")
        return

    percent = battery.percent
    charging = battery.power_plugged
    secs_left = battery.secsleft

    time_str = "N/A"
    if secs_left not in [psutil.POWER_TIME_UNLIMITED, psutil.POWER_TIME_UNKNOWN]:
        hrs = secs_left // 3600
        mins = (secs_left % 3600) // 60
        time_str = f"{hrs}h {mins}m remaining"

    charge_status = "Charging" if charging else "Discharging"
    status_label.config(text=f"Battery: {percent:.1f}% ({charge_status})")
    time_label.config(text=f"Estimated time left: {time_str}")

    # Alerts
    if not charging and percent <= 20:
        status_label.config(fg="red")
        messagebox.showwarning("Battery Low", f"Battery is low: {percent}%")
    elif charging and percent == 100:
        status_label.config(fg="green")
        messagebox.showinfo("Battery Full", "Battery is fully charged.")
    else:
        status_label.config(fg="black")

    # Append for graph
    timestamps.append(datetime.now().strftime("%H:%M:%S"))
    battery_levels.append(percent)

    if len(timestamps) > MAX_POINTS:
        timestamps.pop(0)
        battery_levels.pop(0)

    # Plot
    ax.clear()
    ax.plot(timestamps, battery_levels, marker='o', color='blue')
    ax.set_title("Battery Level Over Time")
    ax.set_ylabel("Battery %")
    ax.set_ylim(0, 100)
    plt.xticks(rotation=45)
    canvas.draw()

    # Log
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%H:%M:%S"), percent, charge_status, time_str])

    root.after(60000, update_battery)  # Update every 60 seconds

# ------------------- Start ------------------- #
update_battery()
root.mainloop()
