# ✅ 5. Animated Object Mover
# Scenario: Animate an object horizontally across a canvas.
# Features:
# •	Use Canvas and .create_rectangle().
# •	Animate using .after() and .move().
# •	Spinbox to set animation speed.
# •	Start/Stop buttons with pack() or grid() layout.

import tkinter as tk

def start_animation():
    global moving
    moving = True
    move_rectangle()

def stop_animation():
    global moving
    moving = False

def move_rectangle():
    global moving
    if moving:
        speed = int(speed_spinbox.get())
        canvas.move(rect, speed, 0)
        x1, y1, x2, y2 = canvas.coords(rect)
        if x2 >= canvas.winfo_width():
            canvas.move(rect, -canvas.winfo_width(), 0)
        root.after(50, move_rectangle)

root = tk.Tk()
root.title("Animated Object Mover")
root.geometry("500x300")

canvas = tk.Canvas(root, width=480, height=200, bg="white")
canvas.pack(pady=10)

rect = canvas.create_rectangle(10, 80, 60, 130, fill="blue")

control_frame = tk.Frame(root)
control_frame.pack()

speed_label=tk.Label(control_frame, text="Speed:")
speed_label.grid(row=0, column=0, padx=5)
speed_spinbox = tk.Spinbox(control_frame, from_=1, to=20, width=5)
speed_spinbox.grid(row=0, column=1, padx=5)
speed_spinbox.delete(0, tk.END)
speed_spinbox.insert(0, "5")

start_btn = tk.Button(control_frame, text="Start", command=start_animation)
start_btn.grid(row=0, column=2, padx=10)

stop_btn = tk.Button(control_frame, text="Stop", command=stop_animation)
stop_btn.grid(row=0, column=3, padx=10)

moving = False

root.mainloop()
