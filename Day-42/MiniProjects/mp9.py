# 🔷 9. Canvas Whiteboard with Shape Insertion
# Widgets Used: Canvas, Listbox, Combobox
# Requirements:
# •	Draw pre-defined shapes (from Listbox) onto canvas (circle, rectangle).
# •	Select color via Combobox.
# •	Delete selected shape from canvas and list.
# •	Undo/redo drawing actions.
# •	Save canvas state to a file (optional).

import tkinter as tk
from tkinter import ttk
import json  # For optional save/load

root = tk.Tk()
root.title("🔷 Canvas Whiteboard")
root.geometry("700x500")

# === Data === #
shapes_drawn = []
redo_stack = []

# === Canvas === #
canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# === Controls === #
control_frame = tk.Frame(root)
control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

# Shape selector
tk.Label(control_frame, text="Select Shape").pack()
shape_listbox = tk.Listbox(control_frame, height=5, exportselection=False)
for shape in ["Circle", "Rectangle"]:
    shape_listbox.insert(tk.END, shape)
shape_listbox.pack(pady=5)

# Color selector
tk.Label(control_frame, text="Select Color").pack()
color_combo = ttk.Combobox(control_frame, values=["red", "green", "blue", "orange", "black"], state="readonly")
color_combo.set("black")
color_combo.pack(pady=5)

# Action log list
tk.Label(control_frame, text="Drawn Shapes").pack()
log_listbox = tk.Listbox(control_frame, height=10)
log_listbox.pack(pady=5)

# === Functions === #
def draw_shape(event=None):
    selection = shape_listbox.curselection()
    if not selection:
        return
    shape = shape_listbox.get(selection)
    color = color_combo.get()
    x, y = event.x, event.y
    size = 40
    obj_id = None

    if shape == "Circle":
        obj_id = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
    elif shape == "Rectangle":
        obj_id = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=color)

    if obj_id:
        info = {"id": obj_id, "type": shape, "x": x, "y": y, "color": color}
        shapes_drawn.append(info)
        redo_stack.clear()  # Reset redo
        log_listbox.insert(tk.END, f"{shape} at ({x}, {y}) [{color}]")

def delete_selected():
    selection = log_listbox.curselection()
    if not selection:
        return
    index = selection[0]
    shape_info = shapes_drawn.pop(index)
    canvas.delete(shape_info["id"])
    log_listbox.delete(index)
    redo_stack.clear()

def undo():
    if shapes_drawn:
        shape = shapes_drawn.pop()
        canvas.delete(shape["id"])
        log_listbox.delete(tk.END)
        redo_stack.append(shape)

def redo():
    if redo_stack:
        shape = redo_stack.pop()
        x, y = shape["x"], shape["y"]
        size = 40
        color = shape["color"]
        shape_type = shape["type"]

        if shape_type == "Circle":
            obj_id = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color)
        elif shape_type == "Rectangle":
            obj_id = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=color)

        shape["id"] = obj_id
        shapes_drawn.append(shape)
        log_listbox.insert(tk.END, f"{shape_type} at ({x}, {y}) [{color}]")

# === Optional Save/Load (commented) === #
def save_to_file():
    data = shapes_drawn
    with open("canvas_save.json", "w") as f:
        json.dump(data, f)

# === Buttons === #
tk.Button(control_frame, text="Delete Selected", command=delete_selected).pack(pady=5)
tk.Button(control_frame, text="Undo", command=undo).pack(pady=5)
tk.Button(control_frame, text="Redo", command=redo).pack(pady=5)
# tk.Button(control_frame, text="Save", command=save_to_file).pack(pady=5)

# === Bind Events === #
canvas.bind("<Button-1>", draw_shape)

root.mainloop()

