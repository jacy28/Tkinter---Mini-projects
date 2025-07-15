# 🕐 5. Digital Clock GUI
# Goal: Display a live updating digital clock in a window.
# Requirements:
# •	Use Label to show time.
# •	Update using after() every second.
# •	Center label using place(relx=0.5, rely=0.5, anchor="center").
# •	Use geometry() to set size and disable resizing.

import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")  # Format: HH:MM:SS
    time_label.config(text=current_time)
    root.after(1000, update_time)  # Call again after 1000 ms (1 second)

# --- GUI Setup ---
root = tk.Tk()
root.title("🕐 Digital Clock")
root.geometry("300x150")
root.resizable(False, False)  # Disable resizing

# --- Time Label ---
time_label = tk.Label(root, font=("Arial", 40), fg="white", bg="black")
time_label.place(relx=0.5, rely=0.5, anchor="center")  # Center label

update_time()  # Start clock updates
root.mainloop()
