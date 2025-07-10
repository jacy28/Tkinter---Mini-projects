# ✅ 18. Hover Tooltip Using Labels
# Objective: Display extra info when hovering over a widget.
# Features:
# •	Use <Enter> to show a tooltip Label.
# •	Use <Leave> to hide it.
# •	Create a function that can be reused with different widgets.

import tkinter as tk

def create_tooltip(widget, text):
    tooltip = tk.Label(widget, text=text, bg="yellow", relief="solid", bd=1, font=("Arial", 10))
    def on_enter(event):
        tooltip.place(x=widget.winfo_x() + widget.winfo_width() + 5,
                      y=widget.winfo_y())
    def on_leave(event):
        tooltip.place_forget()
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

root = tk.Tk()
root.geometry("300x150")

btn = tk.Button(root, text="Hover me")
btn.pack(pady=30)

create_tooltip(btn, "Click to do something!")

root.mainloop()
