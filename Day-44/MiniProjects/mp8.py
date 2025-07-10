# ✅ 8. Counter with Custom Widget
# Objective: Build a class-based counter widget.
# Features:
# •	Custom Frame widget with increment, decrement, and reset buttons.
# •	Label to show current count.
# •	Use .config() to change Label value.

import tkinter as tk

class Counter(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.count = 0
        self.label = tk.Label(self, text="0", width=5, font=("Arial", 16))
        self.label.pack(pady=5)

        btn_frame = tk.Frame(self)
        btn_frame.pack()

        tk.Button(btn_frame, text="+", command=self.increment, width=5).grid(row=0, column=0, padx=2)
        tk.Button(btn_frame, text="-", command=self.decrement, width=5).grid(row=0, column=1, padx=2)
        tk.Button(btn_frame, text="Reset", command=self.reset, width=5).grid(row=0, column=2, padx=2)

    def increment(self):
        self.count += 1
        self.label.config(text=str(self.count))

    def decrement(self):
        self.count -= 1
        self.label.config(text=str(self.count))

    def reset(self):
        self.count = 0
        self.label.config(text=str(self.count))

root = tk.Tk()
root.geometry("300x200")

counter = Counter(root)
counter.pack(pady=20)

root.mainloop()
