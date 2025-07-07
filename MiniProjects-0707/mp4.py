# ✅ 4. Shape Drawing Canvas with Selection
# Scenario: User selects a shape and draws it on canvas by clicking.
# Features:
# •	Combobox to select shape.
# •	Canvas to draw shape at mouse click using bind("<Button-1>").
# •	Display coordinates in a Label.
# •	Use .create_oval(), .create_rectangle() etc.

import tkinter as tk
from tkinter import ttk

def draw_shape(event):
    x, y = event.x, event.y
    shape = shape_combo.get()
    size = 40

    if shape == "Oval":
        canvas.create_oval(x - size, y - size, x + size, y + size, fill="skyblue")
    elif shape == "Rectangle":
        canvas.create_rectangle(x - size, y - size, x + size, y + size, fill="lightgreen")

    coord_label.config(text=f"Coordinates: ({x}, {y})")

root = tk.Tk()
root.title("Shape Drawing Canvas")
root.geometry("500x500")

shape_label = tk.Label(root, text="Select Shape:")
shape_label.pack(pady=5)

shape_combo = ttk.Combobox(root, values=["Oval", "Rectangle"])
shape_combo.current(0)
shape_combo.pack()

canvas = tk.Canvas(root, bg="white", width=480, height=400)
canvas.pack(pady=10)
canvas.bind("<Button-1>", draw_shape)

coord_label = tk.Label(root, text="Coordinates: ( , )")
coord_label.pack()

root.mainloop()
