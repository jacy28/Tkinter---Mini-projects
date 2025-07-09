# ✅ 15. Settings Manager with Side Navigation
# Objective: Preferences window with navigation.
# Requirements:
# •	Use PanedWindow: left for categories, right for settings.
# •	Frame on right changes content based on selection.
# •	Use Label, Checkbutton, Spinbox.
# •	Show confirmation messagebox on Save.

import tkinter as tk
from tkinter import messagebox

def show_settings(category):
    for widget in right_frame.winfo_children():
        widget.destroy()

    if category == "General":
        tk.Label(right_frame, text="General Settings", font=("Arial", 14)).pack(pady=10)
        tk.Checkbutton(right_frame, text="Enable notifications").pack(anchor="w", padx=20, pady=5)
        tk.Checkbutton(right_frame, text="Auto update").pack(anchor="w", padx=20, pady=5)

    elif category == "Display":
        tk.Label(right_frame, text="Display Settings", font=("Arial", 14)).pack(pady=10)
        tk.Label(right_frame, text="Font Size:").pack(anchor="w", padx=20)
        tk.Spinbox(right_frame, from_=8, to=30).pack(anchor="w", padx=20, pady=5)
        tk.Checkbutton(right_frame, text="Dark Mode").pack(anchor="w", padx=20, pady=5)

    elif category == "Account":
        tk.Label(right_frame, text="Account Settings", font=("Arial", 14)).pack(pady=10)
        tk.Label(right_frame, text="Username:").pack(anchor="w", padx=20)
        tk.Entry(right_frame).pack(anchor="w", padx=20, pady=5)
        tk.Checkbutton(right_frame, text="Receive newsletters").pack(anchor="w", padx=20, pady=5)

def save_settings():
    messagebox.showinfo("Saved", "Settings have been saved.")

root = tk.Tk()
root.title("Settings Manager")
root.geometry("500x300")

paned = tk.PanedWindow(root, sashrelief="raised")
paned.pack(fill="both", expand=True)

# Left navigation
nav_frame = tk.Frame(paned, bg="#f0f0f0", width=150)
paned.add(nav_frame)

tk.Button(nav_frame, text="General", width=18, command=lambda: show_settings("General")).pack(pady=5)
tk.Button(nav_frame, text="Display", width=18, command=lambda: show_settings("Display")).pack(pady=5)
tk.Button(nav_frame, text="Account", width=18, command=lambda: show_settings("Account")).pack(pady=5)

# Right settings area
right_frame = tk.Frame(paned, bg="white")
paned.add(right_frame)

# Save button
save_btn = tk.Button(root, text="Save Settings", command=save_settings)
save_btn.pack(pady=10)

# Initialize with General settings
show_settings("General")

root.mainloop()
