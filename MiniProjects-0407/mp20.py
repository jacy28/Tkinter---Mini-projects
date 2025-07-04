# 20. Tkinter Learning Dashboard (Beginner Project Tracker)
# Objective: Visual dashboard for tracking learning modules.
# Features:
# •	Use Canvas to draw progress bars.
# •	Listbox for list of completed topics.
# •	Combobox to select module.
# •	Spinbox to rate understanding level (1–10).
# •	Update canvas graphics as user progresses.
# •	Save/load data locally (optional).


import tkinter as tk
from tkinter import ttk

modules = {
    "Variables": 0,
    "Loops": 0,
    "Functions": 0,
    "Widgets": 0,
    "Layouts": 0,
    "Events": 0
}

def update_progress():
    module = module_combo.get()
    rating = int(rating_spinbox.get())
    if module:
        modules[module] = rating
        draw_progress_bars()
        if module not in completed_listbox.get(0, tk.END):
            completed_listbox.insert(tk.END, module)

def draw_progress_bars():
    canvas.delete("all")
    y = 10
    for mod, val in modules.items():
        canvas.create_text(10, y + 10, anchor="w", text=f"{mod}: {val * 10}%", font=("Arial", 10))
        canvas.create_rectangle(100, y, 300, y + 20, fill="white")
        canvas.create_rectangle(100, y, 100 + val * 20, y + 20, fill="green")
        y += 40

def save_data():
    with open("progress.txt", "w") as f:
        for mod, val in modules.items():
            f.write(f"{mod}:{val}\n")

def load_data():
    try:
        with open("progress.txt", "r") as f:
            for line in f:
                mod, val = line.strip().split(":")
                if mod in modules:
                    modules[mod] = int(val)
        draw_progress_bars()
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("Tkinter Learning Dashboard")
root.geometry("500x500")

tk.Label(root, text="Select Module:").pack(pady=(10, 0))
module_combo = ttk.Combobox(root, values=list(modules.keys()), state="readonly")
module_combo.pack()

tk.Label(root, text="Rate Understanding (1-10):").pack(pady=(10, 0))
rating_spinbox = tk.Spinbox(root, from_=1, to=10, width=5)
rating_spinbox.pack()

tk.Button(root, text="Update Progress", command=update_progress).pack(pady=10)

canvas = tk.Canvas(root, width=400, height=200, bg="lightyellow")
canvas.pack(pady=10)

tk.Label(root, text="Completed Topics:").pack()
completed_listbox = tk.Listbox(root, height=6)
completed_listbox.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Save", command=save_data).pack(side="left", padx=10)
tk.Button(btn_frame, text="Load", command=load_data).pack(side="left", padx=10)

load_data()
root.mainloop()
