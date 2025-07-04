# 13. Shape Drawing with Coordinates
# Objective: Show shape and position where clicked.
# Features:
# •	On Canvas, left-click draws circle, right-click draws square.
# •	Use .bind() for mouse events.
# •	Label shows clicked coordinates.
# •	Allow color selection via Combobox.

import tkinter as tk
from tkinter import ttk

def draw_circle(event):
    x, y = event.x, event.y
    r = 20
    color = color_combo.get()
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="black")
    coord_label.config(text=f"Circle at ({x}, {y})")

def draw_square(event):
    x, y = event.x, event.y
    size = 40
    color = color_combo.get()
    half = size // 2
    canvas.create_rectangle(x - half, y - half, x + half, y + half, fill=color, outline="black")
    coord_label.config(text=f"Square at ({x}, {y})")

root = tk.Tk()
root.title("Shape Drawing with Coordinates")
root.geometry("500x400")

color_frame = tk.Frame(root)
color_frame.pack(pady=10)

tk.Label(color_frame, text="Select Color:").pack(side="left", padx=5)
color_combo = ttk.Combobox(color_frame, values=["red", "green", "blue", "yellow", "purple", "black"], state="readonly")
color_combo.pack(side="left")
color_combo.set("red")


canvas = tk.Canvas(root, bg="white", width=480, height=300)
canvas.pack(padx=10, pady=10)

canvas.bind("<Button-1>", draw_circle)   
canvas.bind("<Button-3>", draw_square)   

coord_label = tk.Label(root, text="Click on the canvas to draw a shape.")
coord_label.pack(pady=(0, 10))

root.mainloop()
