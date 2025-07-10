# ✅ 3. Live Key Press Tracker
# Objective: Display which keyboard key is currently being pressed.
# Features:
# •	Bind <KeyPress> on the root window.
# •	Show key name (event.keysym) in a dynamic Label.
# •	Use Text widget to log each pressed key.
# •	Add <Escape> to close the window.

import tkinter as tk

def on_key_press(event):
    current_key.set(f"Pressed: {event.keysym}")
    log.insert(tk.END, f"{event.keysym}\n")
    log.see(tk.END)
    if event.keysym == "Escape":
        root.destroy()

root = tk.Tk()
root.geometry("300x300")

current_key = tk.StringVar()
label = tk.Label(root, textvariable=current_key, font=("Arial", 14))
label.pack(pady=10)

log = tk.Text(root, height=10, width=30)
log.pack()

root.bind("<KeyPress>", on_key_press)
root.mainloop()
