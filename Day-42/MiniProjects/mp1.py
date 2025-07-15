# 🔷 1. Drawing Tool Application
# Widgets Used: Canvas, Combobox, Spinbox
# Requirements:
# •	Let the user choose shape (rectangle, circle, line) via Combobox.
# •	Select color from another Combobox.
# •	Use Spinbox to select size or thickness of lines.
# •	Click on canvas to draw the selected shape.
# •	Clear all drawings with a "Clear Canvas" button.

import tkinter as tk
from tkinter import ttk

def draw_shape(event):
    shape = shape_combo.get()
    color = color_combo.get()
    size = int(size_spin.get())
    x, y = event.x, event.y

    if shape == "Circle":
        canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline=color)
    elif shape == "Rectangle":
        canvas.create_rectangle(x-size, y-size, x+size, y+size, fill=color, outline=color)
    elif shape == "Line":
        canvas.create_line(x-size, y-size, x+size, y+size, fill=color, width=size)

def clear_canvas():
    canvas.delete("all")

# Main window
root = tk.Tk()
root.geometry("600x500")
root.title("🔷 Drawing Tool")

# Frame for controls
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Shape selection
tk.Label(control_frame, text="Shape:").grid(row=0, column=0, padx=5)
shape_combo = ttk.Combobox(control_frame, values=["Rectangle", "Circle", "Line"], state="readonly", width=10)
shape_combo.current(0)
shape_combo.grid(row=0, column=1, padx=5)

# Color selection
tk.Label(control_frame, text="Color:").grid(row=0, column=2, padx=5)
color_combo = ttk.Combobox(control_frame, values=["red", "green", "blue", "black", "orange"], state="readonly", width=10)
color_combo.current(0)
color_combo.grid(row=0, column=3, padx=5)

# Size/thickness
tk.Label(control_frame, text="Size/Thickness:").grid(row=0, column=4, padx=5)
size_spin = tk.Spinbox(control_frame, from_=1, to=50, width=5)
size_spin.grid(row=0, column=5, padx=5)

# Clear button
clear_btn = tk.Button(control_frame, text="Clear Canvas", command=clear_canvas)
clear_btn.grid(row=0, column=6, padx=10)

# Canvas for drawing
canvas = tk.Canvas(root, bg="white", width=580, height=400)
canvas.pack(pady=10)
canvas.bind("<Button-1>", draw_shape)

root.mainloop()
