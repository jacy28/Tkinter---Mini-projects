# ✅ 11. Timer with Start/Stop Button States
# Objective: Start a timer and disable "Start" button while it's running.
# Features:
# •	Start/Stop/Reset buttons.
# •	Timer displayed using Label.
# •	Disable Start while timer is active, enable Stop.

import tkinter as tk

def update_timer():
    global seconds, running, after_id
    if running:
        seconds += 1
        timer_label.config(text=str(seconds))
        after_id = root.after(1000, update_timer)

def start_timer():
    global running
    if not running:
        running = True
        update_timer()
        start_btn.config(state="disabled")
        stop_btn.config(state="normal")

def stop_timer():
    global running
    if running:
        running = False
        root.after_cancel(after_id)
        start_btn.config(state="normal")
        stop_btn.config(state="disabled")

def reset_timer():
    global seconds
    stop_timer()
    seconds = 0
    timer_label.config(text="0")

root = tk.Tk()
root.geometry("300x200")

seconds = 0
running = False
after_id = None

timer_label = tk.Label(root, text="0", font=("Arial", 24))
timer_label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

start_btn = tk.Button(btn_frame, text="Start", command=start_timer)
start_btn.grid(row=0, column=0, padx=5)

stop_btn = tk.Button(btn_frame, text="Stop", command=stop_timer, state="disabled")
stop_btn.grid(row=0, column=1, padx=5)

reset_btn = tk.Button(btn_frame, text="Reset", command=reset_timer)
reset_btn.grid(row=0, column=2, padx=5)

root.mainloop()
