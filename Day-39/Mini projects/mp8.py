# 8.	Simple Survey App
# 	Use Labels, Entries, and Buttons to collect user feedback (e.g., name, age, favorite color), and display a summary when submitted.

import tkinter as tk
from tkinter import messagebox

def submit_survey():
    name = name_entry.get()
    age = age_entry.get()
    color = color_entry.get()

    if not name or not age or not color:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    summary = f"Survey Submitted!\n\nName: {name}\nAge: {age}\nFavorite Color: {color}"
    messagebox.showinfo("Survey Summary", summary)

    # Clear inputs
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    color_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Simple Survey App")
root.geometry("400x250")

# Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
age_entry = tk.Entry(root, width=30)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Favorite Color:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
color_entry = tk.Entry(root, width=30)
color_entry.grid(row=2, column=1)

# Submit Button
submit_btn = tk.Button(root, text="Submit Survey", command=submit_survey)
submit_btn.grid(row=3, column=1, pady=20, sticky="e")

root.mainloop()
