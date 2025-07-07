# ✅ 19. Countdown Timer with Canvas
# Scenario: Set a countdown and animate it.
# Features:
# •	Spinbox for duration.
# •	Canvas to show animation (shrinking bar).
# •	Start/Pause/Reset buttons.
# •	Time remaining shown in Label.

import tkinter as tk

def start_timer():
    global running
    if not running:
        running = True
        countdown()

def pause_timer():
    global running
    running = False

def reset_timer():
    global running, time_left
    running = False
    time_left = int(duration_spinbox.get())
    update_display()
    reset_bar()

def countdown():
    global running, time_left
    if running and time_left > 0:
        time_left -= 1
        update_display()
        update_bar()
        root.after(1000, countdown)
    elif time_left == 0:
        running = False

def update_display():
    time_label.config(text=f"Time Left: {time_left}s")

def reset_bar():
    canvas.coords(bar, 10, 10, 390, 40)

def update_bar():
    full_width = 380
    new_width = int(full_width * (time_left / int(duration_spinbox.get())))
    canvas.coords(bar, 10, 10, 10 + new_width, 40)

root = tk.Tk()
root.title("Countdown Timer with Canvas")
root.geometry("400x250")

tk.Label(root, text="Set Time (sec):").pack(pady=5)
duration_spinbox = tk.Spinbox(root, from_=5, to=300, width=5)
duration_spinbox.pack()

canvas = tk.Canvas(root, width=400, height=50, bg="white")
canvas.pack(pady=20)
bar = canvas.create_rectangle(10, 10, 390, 40, fill="skyblue")

time_label = tk.Label(root, text="Time Left: 0s", font=("Arial", 14))
time_label.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Start", width=8, command=start_timer).pack(side="left", padx=5)
tk.Button(btn_frame, text="Pause", width=8, command=pause_timer).pack(side="left", padx=5)
tk.Button(btn_frame, text="Reset", width=8, command=reset_timer).pack(side="left", padx=5)

running = False
time_left = int(duration_spinbox.get())
reset_timer()

root.mainloop()
