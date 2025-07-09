# ✅ 5. Tabbed Settings Panel
# Objective: Simulate a settings configuration panel.
# Requirements:
# •	Create a Menu with Edit > Preferences.
# •	On clicking "Preferences", open a Toplevel dialog with frames: 
# o	Frame 1: Account settings
# o	Frame 2: Theme & appearance
# o	Frame 3: Notifications
# •	Use Label, Entry, Checkbutton in each frame.

import tkinter as tk
from tkinter import Toplevel

def open_preferences():
    pref_win = Toplevel(root)
    pref_win.title("Preferences")
    pref_win.geometry("400x350")

    notebook = tk.Frame(pref_win)
    notebook.pack(fill="both", expand=True)

    # Account Settings Frame
    account_frame = tk.LabelFrame(notebook, text="Account Settings", padx=10, pady=10)
    account_frame.pack(fill="both", expand=True, padx=10, pady=5)

    tk.Label(account_frame, text="Username:").grid(row=0, column=0, sticky="w", pady=5)
    tk.Entry(account_frame).grid(row=0, column=1, pady=5)

    tk.Label(account_frame, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
    tk.Entry(account_frame).grid(row=1, column=1, pady=5)

    # Theme Settings Frame
    theme_frame = tk.LabelFrame(notebook, text="Theme & Appearance", padx=10, pady=10)
    theme_frame.pack(fill="both", expand=True, padx=10, pady=5)

    tk.Checkbutton(theme_frame, text="Dark Mode").pack(anchor="w")
    tk.Checkbutton(theme_frame, text="Enable animations").pack(anchor="w")

    # Notifications Frame
    notify_frame = tk.LabelFrame(notebook, text="Notifications", padx=10, pady=10)
    notify_frame.pack(fill="both", expand=True, padx=10, pady=5)

    tk.Checkbutton(notify_frame, text="Email Notifications").pack(anchor="w")
    tk.Checkbutton(notify_frame, text="Push Notifications").pack(anchor="w")
    tk.Checkbutton(notify_frame, text="SMS Alerts").pack(anchor="w")

    tk.Button(pref_win, text="Save", width=10, command=pref_win.destroy).pack(pady=10)

root = tk.Tk()
root.title("Settings Panel")
root.geometry("400x200")

menu_bar = tk.Menu(root)
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Preferences", command=open_preferences)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
root.config(menu=menu_bar)

tk.Label(root, text="Main Application Window", font=("Arial", 14)).pack(expand=True)

root.mainloop()
