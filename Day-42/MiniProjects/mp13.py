# 🔷 13. Timer with Canvas Display
# Widgets Used: Canvas, Spinbox, Button
# Requirements:
# •	Spinbox to set countdown time in seconds.
# •	Button to start timer.
# •	Display countdown on canvas with animated circle shrinking.
# •	Sound alert when time completes.
# •	Pause/resume support.

import tkinter as tk
import time
import threading
import platform
import os

root = tk.Tk()
root.title("🔷 Canvas Timer")
root.geometry("400x400")

# --- Global Variables ---
timer_running = False
paused = False
time_left = 0
circle = None
text = None

# --- Beep Sound Function ---
def play_beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 500)
    else:
        os.system('say "Time is up"')  # macOS
        # For Linux you can use: os.system('beep')

# --- Timer Logic ---
def start_timer():
    global timer_running, time_left, paused
    if timer_running:
        return
    timer_running = True
    paused = False
    time_left = int(spinbox.get())
    update_canvas()
    countdown()

def pause_resume():
    global paused
    if not timer_running:
        return
    paused = not paused
    pause_btn.config(text="Resume" if paused else "Pause")
    if not paused:
        countdown()

def countdown():
    global time_left, timer_running
    if paused or not timer_running:
        return
    if time_left <= 0:
        canvas.itemconfig(text, text="Time's Up!", fill="red")
        play_beep()
        timer_running = False
        return
    canvas.itemconfig(text, text=f"{time_left}s")
    shrink_circle()
    time_left -= 1
    root.after(1000, countdown)

def update_canvas():
    global circle, text
    canvas.delete("all")
    circle = canvas.create_oval(50, 50, 250, 250, fill="skyblue")
    text = canvas.create_text(150, 150, text=f"{time_left}s", font=("Arial", 24), fill="black")

def shrink_circle():
    fraction = time_left / int(spinbox.get())
    new_size = int(200 * fraction)
    x0 = 150 - new_size // 2
    y0 = 150 - new_size // 2
    x1 = 150 + new_size // 2
    y1 = 150 + new_size // 2
    canvas.coords(circle, x0, y0, x1, y1)

# --- UI Layout ---
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Set Time (s):").pack(side=tk.LEFT)
spinbox = tk.Spinbox(top_frame, from_=1, to=300, width=5)
spinbox.pack(side=tk.LEFT, padx=5)

start_btn = tk.Button(top_frame, text="Start", command=start_timer)
start_btn.pack(side=tk.LEFT, padx=5)

pause_btn = tk.Button(top_frame, text="Pause", command=pause_resume)
pause_btn.pack(side=tk.LEFT, padx=5)

canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Start with placeholder circle
circle = canvas.create_oval(50, 50, 250, 250, fill="skyblue")
text = canvas.create_text(150, 150, text="Ready", font=("Arial", 24), fill="black")

root.mainloop()
