# ✅ 4. Dynamic Color Picker
# Objective: Change the background color of a frame based on arrow keys.
# Features:
# •	Use <Left>, <Right>, <Up>, <Down> bindings.
# •	Each direction changes the frame’s bg color.
# •	Include a Label showing the current color name.

import tkinter as tk

def change_color(event):
    color_map = {
        "Left": "red",
        "Right": "green",
        "Up": "blue",
        "Down": "yellow"
    }
    if event.keysym in color_map:
        color = color_map[event.keysym]
        frame.config(bg=color)
        color_label.config(text=f"Color: {color}")

root = tk.Tk()
root.geometry("300x300")

frame = tk.Frame(root, width=200, height=200, bg="white")
frame.pack(pady=20)

color_label = tk.Label(root, text="Color: white", font=("Arial", 12))
color_label.pack()

root.bind("<Left>", change_color)
root.bind("<Right>", change_color)
root.bind("<Up>", change_color)
root.bind("<Down>", change_color)

root.mainloop()
