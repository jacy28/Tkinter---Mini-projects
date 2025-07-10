# ✅ 5. Shape Drawer Canvas
# Objective: Click to draw shapes and print coordinates.
# Features:
# •	Canvas widget.
# •	On <Button-1> click, draw a circle at cursor position.
# •	On <Button-3> click, draw a rectangle.
# •	Show (x, y) position in a Label.

import tkinter as tk

def draw_shape(event):
    x, y = event.x, event.y
    coord_label.config(text=f"Coordinates: ({x}, {y})")
    if event.num == 1:
        canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")
    elif event.num == 3:
        canvas.create_rectangle(x-10, y-10, x+10, y+10, fill="red")

root = tk.Tk()
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white", width=300, height=300)
canvas.pack(pady=10)
canvas.bind("<Button-1>", draw_shape)
canvas.bind("<Button-3>", draw_shape)

coord_label = tk.Label(root, text="Coordinates: ")
coord_label.pack()

root.mainloop()
