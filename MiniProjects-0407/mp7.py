# 7. Animated Moving Object
# Objective: Animate a rectangle on canvas.
# Features:
# •	Use Canvas and create_rectangle().
# •	Animate using .after() loop.
# •	Use Spinbox to control speed.
# •	Start/Stop buttons.
# •	Display object’s current X-Y coordinates using Label.

import tkinter as tk

moving = False
rect = None
speed = 50  

def move_rect():
    if moving:
        canvas.move(rect, 5, 0)
        x, y, _, _ = canvas.coords(rect)
        coord_label.config(text=f"X: {int(x)}  Y: {int(y)}")

        if x > canvas.winfo_width():
            canvas.coords(rect, 0, 50, 50, 100)

        root.after(speed, move_rect)

def start():
    global moving, speed
    moving = True
    speed = int(speed_spinbox.get())
    move_rect()

def stop():
    global moving
    moving = False

root = tk.Tk()
root.title("Simple Animation")

canvas = tk.Canvas(root, width=400, height=150, bg="white")
canvas.pack(pady=10)

rect = canvas.create_rectangle(0, 50, 50, 100, fill="blue")

speed_spinbox = tk.Spinbox(root, from_=10, to=200, width=5)
speed_spinbox.pack()
speed_spinbox.delete(0, "end")
speed_spinbox.insert(0, "50")

tk.Button(root, text="Start", command=start).pack(side="left", padx=10, pady=10)
tk.Button(root, text="Stop", command=stop).pack(side="left", padx=10)

coord_label = tk.Label(root, text="X: 0  Y: 50")
coord_label.pack()

root.mainloop()
