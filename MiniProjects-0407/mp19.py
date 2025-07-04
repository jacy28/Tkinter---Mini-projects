
# 19. Custom Window Configurator
# Objective: Set window size, title, and icon dynamically.
# Features:
# •	Use Entry widgets to take title, width, height.
# •	Button to apply the changes using .geometry() and .title().
# •	Optional file input for .iconbitmap().
# •	place() for exact control of layout.


import tkinter as tk
from tkinter import filedialog

def apply_config():
    title = title_entry.get()
    width = width_entry.get()
    height = height_entry.get()
    icon_path = icon_entry.get()

    if title:
        root.title(title)
    if width.isdigit() and height.isdigit():
        root.geometry(f"{width}x{height}")
    if icon_path:
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            error_label.config(text="Invalid icon file.")

def browse_icon():
    file_path = filedialog.askopenfilename(
        filetypes=[("Icon files", "*.ico")])
    if file_path:
        icon_entry.delete(0, tk.END)
        icon_entry.insert(0, file_path)

root = tk.Tk()
root.title("Window Configurator")
root.geometry("400x300")

tk.Label(root, text="Title:").place(x=30, y=30)
title_entry = tk.Entry(root, width=30)
title_entry.place(x=130, y=30)

tk.Label(root, text="Width:").place(x=30, y=70)
width_entry = tk.Entry(root, width=10)
width_entry.place(x=130, y=70)

tk.Label(root, text="Height:").place(x=200, y=70)
height_entry = tk.Entry(root, width=10)
height_entry.place(x=260, y=70)

tk.Label(root, text="Icon Path:").place(x=30, y=110)
icon_entry = tk.Entry(root, width=25)
icon_entry.place(x=130, y=110)
browse_btn = tk.Button(root, text="Browse", command=browse_icon)
browse_btn.place(x=300, y=108)

apply_btn = tk.Button(root, text="Apply Settings", command=apply_config)
apply_btn.place(x=150, y=160)

error_label = tk.Label(root, text="", fg="red")
error_label.place(x=130, y=200)

root.mainloop()
