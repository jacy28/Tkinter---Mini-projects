# 🟢 6. Shape Animation Simulator
# Goal: Animate a shape across canvas.
# Requirements:
# •	Draw a rectangle on Canvas.
# •	Move it left to right using .move() and .after().
# •	Use Spinbox to set speed.
# •	Buttons to Start, Pause, Reset.
# •	Use Frame to group canvas and controls.

import tkinter as tk

root = tk.Tk()
root.title("Shape Animation Simulator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

canvas = tk.Canvas(frame, width=400, height=200, bg="white")
canvas.pack()

rect = canvas.create_rectangle(10, 80, 60, 130, fill="blue")

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

speed_label = tk.Label(control_frame, text="Speed (ms):")
speed_label.grid(row=0, column=0, padx=5)

speed_spinbox = tk.Spinbox(control_frame, from_=10, to=1000, increment=10)
speed_spinbox.grid(row=0, column=1, padx=5)
speed_spinbox.delete(0, tk.END)
speed_spinbox.insert(0, "50")

is_running = False
animation_id = None

def animate():
    global animation_id
    if is_running:
        canvas.move(rect, 5, 0)
        x1, _, x2, _ = canvas.coords(rect)
        if x2 >= canvas.winfo_width():
            return
        delay = int(speed_spinbox.get())
        animation_id = root.after(delay, animate)

def start():
    global is_running
    if not is_running:
        is_running = True
        animate()

def pause():
    global is_running, animation_id
    if animation_id:
        root.after_cancel(animation_id)
    is_running = False

def reset():
    global is_running, animation_id
    if animation_id:
        root.after_cancel(animation_id)
    is_running = False
    canvas.coords(rect, 10, 80, 60, 130)

start_btn = tk.Button(control_frame, text="Start", command=start)
start_btn.grid(row=0, column=2, padx=5)

pause_btn = tk.Button(control_frame, text="Pause", command=pause)
pause_btn.grid(row=0, column=3, padx=5)

reset_btn = tk.Button(control_frame, text="Reset", command=reset)
reset_btn.grid(row=0, column=4, padx=5)

root.mainloop()
