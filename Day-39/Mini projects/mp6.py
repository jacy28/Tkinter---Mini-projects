# 6.	Digital Clock
# Label that updates to show the current time every second.

import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)  

# GUI Setup
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")

clock_label = tk.Label(root, text="", font=("Arial", 40), fg="white", bg="black")
clock_label.pack(expand=True)

update_time()  

root.mainloop()
