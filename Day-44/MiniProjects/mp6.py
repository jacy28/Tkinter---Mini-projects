# ✅ 6. Custom Toggle Switch Widget
# Objective: Create a reusable toggle widget using class and Frame.
# Features:
# •	Class-based widget with Button and Label.
# •	Button toggles Label text between “ON” and “OFF”.
# •	Allow multiple instances of this custom widget.

import tkinter as tk

class ToggleSwitch(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.state = False
        self.label = tk.Label(self, text="OFF", width=10)
        self.label.pack(side="left", padx=5)
        self.button = tk.Button(self, text="Toggle", command=self.toggle)
        self.button.pack(side="right", padx=5)

    def toggle(self):
        self.state = not self.state
        self.label.config(text="ON" if self.state else "OFF")

root = tk.Tk()
root.geometry("300x200")

toggle1 = ToggleSwitch(root)
toggle1.pack(pady=10)

toggle2 = ToggleSwitch(root)
toggle2.pack(pady=10)

root.mainloop()
