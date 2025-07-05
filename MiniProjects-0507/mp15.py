# 🟢 15. Window Configuration App
# Goal: Customize window size, title, and icon.
# Requirements:
# •	Entry for window title.
# •	Spinbox for width and height.
# •	Button to apply changes using .geometry() and .title().
# •	Optionally, load icon using .iconbitmap().

import tkinter as tk
from tkinter import messagebox

def apply_config():
    title = title_entry.get()
    width = width_spinbox.get()
    height = height_spinbox.get()
    if not title:
        messagebox.showwarning("Input Error", "Title cannot be empty.")
        return
    root.title(title)
    root.geometry(f"{width}x{height}")
    try:
        root.iconbitmap("app.ico")  
    except:
        pass

root = tk.Tk()
root.title("Window Configurator")
root.geometry("400x250")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20)

title_label = tk.Label(frame, text="Window Title:")
title_label.grid(row=0, column=0, sticky="w", pady=5)
title_entry = tk.Entry(frame, width=25)
title_entry.grid(row=0, column=1, pady=5)

width_label = tk.Label(frame, text="Width:")
width_label.grid(row=1, column=0, sticky="w", pady=5)
width_spinbox = tk.Spinbox(frame, from_=200, to=1000, width=10)
width_spinbox.grid(row=1, column=1, pady=5, sticky="w")

height_label = tk.Label(frame, text="Height:")
height_label.grid(row=2, column=0, sticky="w", pady=5)
height_spinbox = tk.Spinbox(frame, from_=200, to=800, width=10)
height_spinbox.grid(row=2, column=1, pady=5, sticky="w")

apply_btn = tk.Button(root, text="Apply Settings", command=apply_config)
apply_btn.grid(row=1, column=0, pady=10)

root.mainloop()
