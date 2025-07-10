# ✅ 9. Mouse Hover UI Effects
# Objective: Change the color of labels/buttons on hover.
# Features:
# •	Bind <Enter> and <Leave> on Label and Button.
# •	Change foreground or background color dynamically.
# •	Reset to original style on leave.

import tkinter as tk

def on_enter(event):
    event.widget.config(bg="lightblue", fg="black")

def on_leave(event):
    event.widget.config(bg=original_bg, fg=original_fg)

root = tk.Tk()
root.geometry("300x200")

original_bg = root.cget("bg")
original_fg = "black"

label = tk.Label(root, text="Hover over me", bg=original_bg, fg=original_fg, font=("Arial", 12))
label.pack(pady=10)
label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

button = tk.Button(root, text="Hover Button", bg=original_bg, fg=original_fg, font=("Arial", 12))
button.pack(pady=10)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()
