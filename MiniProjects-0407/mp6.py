# 6. Canvas Drawing Shapes Tool
# Objective: Draw selected shapes on canvas at mouse click.
# Features:
# •	Canvas widget with create_rectangle(), create_oval().
# •	Shape type selected via Combobox.
# •	Color selection via another Combobox.
# •	On <Button-1>, draw the selected shape at cursor point.

import tkinter as tk
from tkinter import ttk

def draw_shape(event):
    shape = shape_combo.get()
    color = color_combo.get()
    x, y = event.x, event.y
    size = 40  

    if shape == "Rectangle":
        canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline="")
    elif shape == "Oval":
        canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")

root = tk.Tk()
root.title("Canvas Drawing Tool")
root.geometry("500x400")

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Shape:").pack(side="left", padx=5)
shape_combo = ttk.Combobox(control_frame, values=["Rectangle", "Oval"], state="readonly", width=10)
shape_combo.pack(side="left", padx=5)
shape_combo.set("Rectangle")

tk.Label(control_frame, text="Color:").pack(side="left", padx=5)
color_combo = ttk.Combobox(control_frame, values=["red", "green", "blue", "yellow", "black"], state="readonly", width=10)
color_combo.pack(side="left", padx=5)
color_combo.set("red")

canvas = tk.Canvas(root, bg="white", width=480, height=300)
canvas.pack(pady=10)

canvas.bind("<Button-1>", draw_shape)

root.mainloop()
