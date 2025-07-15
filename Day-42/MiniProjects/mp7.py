# 🔷 7. Simple Drawing Game (Click & Draw)
# Widgets Used: Canvas, Combobox, Listbox
# Requirements:
# •	Select object type via Combobox (star, ball, square).
# •	On mouse click, draw object at clicked position.
# •	Listbox logs each drawing action (with coordinates).
# •	"Undo" button removes last drawn object.
# •	Scrollbar if log exceeds 10 lines.

import tkinter as tk
from tkinter import ttk
import math  # Import math for sin, cos, radians

root = tk.Tk()
root.title("🔷 Simple Drawing Game (Click & Draw)")
root.geometry("750x500")

# ------------------ Canvas ------------------ #
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# ------------------ Shape Selection ------------------ #
shape_frame = tk.Frame(root)
shape_frame.pack(pady=10)

tk.Label(shape_frame, text="Select Shape:").pack()

shape_combo = ttk.Combobox(shape_frame, values=["Star", "Ball", "Square"], state="readonly")
shape_combo.set("Ball")
shape_combo.pack(pady=5)

# ------------------ Log and Scrollbar ------------------ #
log_frame = tk.Frame(root)
log_frame.pack()

scrollbar = tk.Scrollbar(log_frame, orient=tk.VERTICAL)
log_listbox = tk.Listbox(log_frame, height=20, width=35, yscrollcommand=scrollbar.set)
scrollbar.config(command=log_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# ------------------ Tracking Drawn Items ------------------ #
drawn_items = []

# ------------------ Drawing Function ------------------ #
def draw_shape(event):
    shape = shape_combo.get()
    x, y = event.x, event.y
    size = 20
    obj_id = None

    if shape == "Ball":
        obj_id = canvas.create_oval(x - size, y - size, x + size, y + size, fill="skyblue")
    elif shape == "Square":
        obj_id = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill="lightgreen")
    elif shape == "Star":
        obj_id = draw_star(x, y, size)

    if obj_id:
        drawn_items.append(obj_id)
        log_listbox.insert(tk.END, f"{shape} at ({x},{y})")
        log_listbox.yview_moveto(1.0)  # Auto scroll to bottom

# ------------------ Star Drawing Helper ------------------ #
def draw_star(x, y, r):
    points = []
    for i in range(5):
        angle_deg = i * 144
        angle_rad = math.radians(angle_deg)
        px = x + r * math.sin(angle_rad)
        py = y - r * math.cos(angle_rad)
        points.extend([px, py])
    return canvas.create_polygon(points, fill="gold", outline="black")

# ------------------ Undo Function ------------------ #
def undo_last():
    if drawn_items:
        last_item = drawn_items.pop()
        canvas.delete(last_item)
        log_listbox.delete(tk.END)

# ------------------ Bind Mouse Click ------------------ #
canvas.bind("<Button-1>", draw_shape)

# ------------------ Undo Button ------------------ #
tk.Button(shape_frame, text="Undo Last", command=undo_last).pack(pady=20)

root.mainloop()
