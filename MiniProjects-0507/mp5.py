# 🟢 5. Drawing Canvas App
# Goal: Draw shapes by clicking.
# Requirements:
# •	Use Canvas for drawing.
# •	Use Combobox to select shape (circle, rectangle).
# •	Bind <Button-1> to draw shape at cursor.
# •	Use color selection via another Combobox.
# •	Display coordinates on click using Label.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Drawing Canvas App")

def draw_shape(event):
    x, y = event.x, event.y
    coords_var.set(f"Coordinates: ({x}, {y})")
    shape = shape_choice.get()
    color = color_choice.get()
    size = 30
    if shape == "Circle":
        canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="")
    elif shape == "Rectangle":
        canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=color, outline="")

shape_choice = ttk.Combobox(root, values=["Circle", "Rectangle"])
shape_choice.set("Circle")
shape_choice.grid(row=0, column=0, padx=5, pady=5)

color_choice = ttk.Combobox(root, values=["red", "green", "blue", "black", "yellow"])
color_choice.set("black")
color_choice.grid(row=0, column=1, padx=5, pady=5)

canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
canvas.bind("<Button-1>", draw_shape)

coords_var = tk.StringVar()
coords_label = tk.Label(root, textvariable=coords_var)
coords_label.grid(row=2, column=0, columnspan=2)

root.mainloop()
