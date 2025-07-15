# 🔷 4. Color Picker App
# Widgets Used: Canvas, Combobox, Event Bind
# Requirements:
# •	Combobox to pick a color (Red, Green, Blue, etc.).
# •	Click anywhere on canvas to paint that area with the selected color.
# •	Bind right-click to erase the color (reset to white).
# •	Display coordinates and color in a Label on click.

import tkinter as tk
from tkinter import ttk

CELL_SIZE = 20  # Size of each "paintable" cell

def draw_grid():
    """Create a grid of rectangles (cells) on the canvas."""
    for y in range(0, canvas_height, CELL_SIZE):
        for x in range(0, canvas_width, CELL_SIZE):
            rect = canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="white", outline="lightgray")
            rect_coords[rect] = (x, y)

def get_cell_id(x, y):
    """Return the rectangle ID at a given pixel position."""
    items = canvas.find_overlapping(x, y, x, y)
    return items[-1] if items else None

def paint_cell(event):
    rect_id = get_cell_id(event.x, event.y)
    if rect_id:
        selected_color = color_combo.get()
        canvas.itemconfig(rect_id, fill=selected_color)
        coords = rect_coords[rect_id]
        info_label.config(text=f"Painted at ({coords[0]}, {coords[1]}) - Color: {selected_color}")

def erase_cell(event):
    rect_id = get_cell_id(event.x, event.y)
    if rect_id:
        canvas.itemconfig(rect_id, fill="white")
        coords = rect_coords[rect_id]
        info_label.config(text=f"Erased at ({coords[0]}, {coords[1]})")

# Main window
root = tk.Tk()
root.title("🔷 Color Picker App")
root.geometry("500x450")

# Color selection Combobox
tk.Label(root, text="Select Color:").pack(pady=5)
color_combo = ttk.Combobox(root, values=["red", "green", "blue", "yellow", "orange", "black"], state="readonly")
color_combo.set("red")
color_combo.pack(pady=5)

# Canvas setup
canvas_width, canvas_height = 400, 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(pady=10)

# Dictionary to store cell coordinates
rect_coords = {}

# Draw initial grid
draw_grid()

# Bind mouse events
canvas.bind("<Button-1>", paint_cell)     # Left click
canvas.bind("<Button-3>", erase_cell)     # Right click

# Label to display info
info_label = tk.Label(root, text="Click a cell to paint or erase.", font=("Arial", 12))
info_label.pack(pady=5)

root.mainloop()
