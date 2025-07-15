# 🎲 15. Dice Roller Simulator
# Goal: Simulate rolling a dice (1-6).
# Requirements:
# •	Use Button to roll.
# •	Show result in Label.
# •	Use random.randint(1, 6).
# •	Center elements using place().

import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f"🎲 {result}", fg="blue")

# Create main window
root = tk.Tk()
root.title("🎲 Dice Roller Simulator")
root.geometry("300x200")
root.resizable(False, False)

# Result label
result_label = tk.Label(root, text="🎲", font=("Arial", 40))
result_label.place(relx=0.5, rely=0.3, anchor="center")

# Roll button
roll_button = tk.Button(root, text="Roll Dice", font=("Arial", 14), command=roll_dice)
roll_button.place(relx=0.5, rely=0.7, anchor="center")

# Start the GUI
root.mainloop()
