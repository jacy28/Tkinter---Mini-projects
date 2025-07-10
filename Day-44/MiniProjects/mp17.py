# ✅ 17. Canvas Object Mover with Keys
# Objective: Move an object using keyboard arrows.
# Features:
# •	Canvas with rectangle or circle.
# •	Bind arrow keys to .move() the object.
# •	Limit boundaries using canvas size check.

import tkinter as tk

def move(event):
    x, y = 0, 0
    if event.keysym == "Up": y = -10
    elif event.keysym == "Down": y = 10
    elif event.keysym == "Left": x = -10
    elif event.keysym == "Right": x = 10

    coords = canvas.coords(obj)
    if 0 <= coords[0]+x and coords[2]+x <= 300 and 0 <= coords[1]+y and coords[3]+y <= 200:
        canvas.move(obj, x, y)

root = tk.Tk()
root.geometry("320x240")
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

obj = canvas.create_oval(130, 80, 170, 120, fill="blue")

root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

root.mainloop()
