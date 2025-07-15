import tkinter as tk
from tkinter import ttk

# Setup main window
root = tk.Tk()
root.title("🔷 Shape Animation Editor")
root.geometry("700x500")

canvas = tk.Canvas(root, width=600, height=350, bg="white")
canvas.pack(pady=10)

# List to track animated shapes
animated_shapes = []

# Dictionary for movement vectors
directions = {
    "Right": (5, 0),
    "Left": (-5, 0),
    "Up": (0, -5),
    "Down": (0, 5)
}

animation_running = False  # Start paused

def animate_shapes():
    if animation_running:
        for shape in animated_shapes:
            dx, dy = shape["vector"]
            canvas.move(shape["id"], dx, dy)
            x1, y1, x2, y2 = canvas.coords(shape["id"])
            
            # Wrap around edges
            if x2 < 0: canvas.move(shape["id"], 600, 0)
            if x1 > 600: canvas.move(shape["id"], -600, 0)
            if y2 < 0: canvas.move(shape["id"], 0, 350)
            if y1 > 350: canvas.move(shape["id"], 0, -350)
        root.after(30, animate_shapes)

def start_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        animate_shapes()

def pause_animation():
    global animation_running
    animation_running = False

def add_shape():
    global animation_running
    shape_type = shape_combo.get()
    direction = direction_combo.get()
    speed = int(speed_spin.get())

    dx, dy = directions[direction]
    dx *= speed // 10
    dy *= speed // 10

    x, y = 50, 50  # Starting point

    if shape_type == "Rectangle":
        shape_id = canvas.create_rectangle(x, y, x+40, y+30, fill="skyblue")
    elif shape_type == "Circle":
        shape_id = canvas.create_oval(x, y, x+30, y+30, fill="lightgreen")
    elif shape_type == "Line":
        shape_id = canvas.create_line(x, y, x+40, y+0, width=3, fill="black")
    else:
        return

    animated_shapes.append({
        "id": shape_id,
        "vector": (dx, dy)
    })

    # Start animation if not running
    if animation_running and len(animated_shapes) == 1:
        animate_shapes()

def stop_all():
    global animated_shapes
    for shape in animated_shapes:
        canvas.delete(shape["id"])
    animated_shapes.clear()

# --- Controls ---
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Shape selector
tk.Label(control_frame, text="Shape:").grid(row=0, column=0, padx=5)
shape_combo = ttk.Combobox(control_frame, values=["Rectangle", "Circle", "Line"], state="readonly", width=10)
shape_combo.set("Rectangle")
shape_combo.grid(row=0, column=1, padx=5)

# Direction selector
tk.Label(control_frame, text="Direction:").grid(row=0, column=2, padx=5)
direction_combo = ttk.Combobox(control_frame, values=list(directions.keys()), state="readonly", width=10)
direction_combo.set("Right")
direction_combo.grid(row=0, column=3, padx=5)

# Speed spinbox
tk.Label(control_frame, text="Speed:").grid(row=0, column=4, padx=5)
speed_spin = tk.Spinbox(control_frame, from_=1, to=50, width=5)
speed_spin.grid(row=0, column=5, padx=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Shape", command=add_shape).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="▶ Start", command=start_animation).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="⏸ Pause", command=pause_animation).grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="🛑 Stop All", command=stop_all).grid(row=0, column=3, padx=10)

root.mainloop()
