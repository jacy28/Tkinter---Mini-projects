# ✅ 15. Entry Field Character Counter
# Objective: Count and display characters as the user types.
# Features:
# •	Entry widget for typing.
# •	Label that updates on every key press.
# •	Use <KeyRelease> to update character count.

import tkinter as tk

def update_count(event=None):
    text = entry.get()
    count_label.config(text=f"Characters: {len(text)}")

root = tk.Tk()
root.geometry("300x150")
root.title("Character Counter")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill="x")
entry.bind("<KeyRelease>", update_count)

count_label = tk.Label(root, text="Characters: 0", font=("Arial", 12))
count_label.pack(pady=5)

root.mainloop()
