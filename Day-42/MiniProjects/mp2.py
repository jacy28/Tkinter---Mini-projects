# 🔷 2. Animation Playground
# Widgets Used: Canvas, Spinbox, Button
# Requirements:
# •	Draw a rectangle on canvas.
# •	Move the rectangle automatically (left to right).
# •	Use Spinbox to control speed of animation (delay in ms).
# •	Use buttons to pause/resume animation.
# •	Display X, Y coordinates of the rectangle while animating.

import tkinter as tk

def move_rectangle():
    global animation_running
    if animation_running:
        canvas.move(rect, 5, 0)
        x1, y1, x2, y2 = canvas.coords(rect)
        coord_label.config(text=f"X: {int(x1)}, Y: {int(y1)}")

        # Reset to left if it goes off the canvas
        if x2 > canvas.winfo_width():
            canvas.coords(rect, 0, y1, 50, y2)

        # Schedule next move
        delay = int(speed_var.get())
        root.after(delay, move_rectangle)

def start_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        move_rectangle()

def pause_animation():
    global animation_running
    animation_running = False

# Main window
root = tk.Tk()
root.geometry("600x400")
root.title("🔷 Animation Playground")

# Canvas
canvas = tk.Canvas(root, width=550, height=250, bg="white")
canvas.pack(pady=10)

# Draw initial rectangle
rect = canvas.create_rectangle(0, 100, 50, 150, fill="skyblue")

# Animation state
animation_running = False

# Speed control (delay in ms)
tk.Label(root, text="Speed (ms):").pack()
speed_var = tk.StringVar(value="100")
speed_spin = tk.Spinbox(root, from_=10, to=1000, increment=10, textvariable=speed_var, width=8)
speed_spin.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

start_btn = tk.Button(btn_frame, text="▶ Resume", command=start_animation, width=10)
start_btn.grid(row=0, column=0, padx=10)

pause_btn = tk.Button(btn_frame, text="⏸ Pause", command=pause_animation, width=10)
pause_btn.grid(row=0, column=1, padx=10)

# Coordinates display
coord_label = tk.Label(root, text="X: 0, Y: 100", font=("Arial", 12))
coord_label.pack(pady=10)

root.mainloop()
