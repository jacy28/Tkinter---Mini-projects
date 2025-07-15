# 🔷 17. Canvas-based Grid Game
# Widgets Used: Canvas, Listbox, Event Bindings
# Requirements:
# •	Create 5x5 grid on Canvas.
# •	User clicks cell to change color (simulate marking).
# •	Listbox logs clicked positions.
# •	Add Reset button.
# •	Scrollbar if logs exceed 10.

import tkinter as tk

# --- Constants ---
CELL_SIZE = 60
GRID_SIZE = 5
CANVAS_WIDTH = CELL_SIZE * GRID_SIZE
CANVAS_HEIGHT = CELL_SIZE * GRID_SIZE

# --- Main window ---
root = tk.Tk()
root.title("🔷 Grid Marking Game")
root.geometry("500x420")

# --- Canvas ---
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.grid(row=0, column=0, padx=10, pady=10)

# --- Draw 5x5 Grid ---
cells = {}  # {(row, col): rect_id}

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
        cells[(row, col)] = rect

# --- Listbox + Scrollbar for logging ---
log_frame = tk.Frame(root)
log_frame.grid(row=0, column=1, sticky="ns", pady=10)

tk.Label(log_frame, text="Click Log").pack()

scrollbar = tk.Scrollbar(log_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_listbox = tk.Listbox(log_frame, height=15, yscrollcommand=scrollbar.set, width=25)
log_listbox.pack()
scrollbar.config(command=log_listbox.yview)

# --- Click Handler ---
marked_cells = set()

def on_canvas_click(event):
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
        cell = (row, col)
        rect_id = cells[cell]
        if cell not in marked_cells:
            canvas.itemconfig(rect_id, fill="lightblue")
            log_listbox.insert(tk.END, f"Marked cell ({row+1}, {col+1})")
            marked_cells.add(cell)

canvas.bind("<Button-1>", on_canvas_click)

# --- Reset Button ---
def reset_grid():
    for cell, rect in cells.items():
        canvas.itemconfig(rect, fill="white")
    log_listbox.delete(0, tk.END)
    marked_cells.clear()

reset_btn = tk.Button(root, text="🔁 Reset Grid", command=reset_grid)
reset_btn.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
