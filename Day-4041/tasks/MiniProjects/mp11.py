# 🎨 11. Color Picker GUI
# Goal: Select a color and apply it as window background.
# Requirements:
# •	Buttons for predefined colors.
# •	Change background using config(bg=color).
# •	Show selected color name in Label.
# •	Layout using pack() and side="left".

import tkinter as tk

# --- Change background color function ---
def change_color(color):
    root.config(bg=color)
    selected_label.config(text=f"Selected Color: {color}", bg=color)

# --- GUI setup ---
root = tk.Tk()
root.title("🎨 Color Picker")
root.geometry("400x200")

# --- Color buttons frame ---
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# --- Predefined colors ---
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# --- Create buttons ---
for color in colors:
    btn = tk.Button(button_frame, text=color.capitalize(), bg=color, fg="white",
                    width=10, command=lambda c=color: change_color(c))
    btn.pack(side="left", padx=5)

# --- Label to show selected color ---
selected_label = tk.Label(root, text="Selected Color: None", font=("Arial", 12))
selected_label.pack(pady=20)

root.mainloop()
