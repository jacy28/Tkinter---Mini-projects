# 7.	Temperature Logger
# 	Entry for temperature input, Button to log, and a multi-line Text widget to display the log.

import tkinter as tk
from tkinter import messagebox

def log_temperature():
    temp = temp_entry.get()
    if temp.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a temperature.")
        return
    log_text.insert(tk.END, f"Logged Temperature: {temp}°C\n")
    temp_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Temperature Logger")
root.geometry("400x300")

# Label & Entry
tk.Label(root, text="Enter Temperature (°C):").pack(pady=10)
temp_entry = tk.Entry(root, width=25)
temp_entry.pack()

# Log Button
log_btn = tk.Button(root, text="Log Temperature", command=log_temperature)
log_btn.pack(pady=10)

# Text Widget with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

log_text = tk.Text(frame, width=40, height=10, yscrollcommand=scrollbar.set)
log_text.pack()

scrollbar.config(command=log_text.yview)

root.mainloop()
