# ✅ 2. Personal Portfolio Dashboard
# Scenario: Create a personal info dashboard with editable fields.
# Features:
# •	Label, Entry, and Text for personal and bio info.
# •	Button to update Label dynamically from input.
# •	Use place() for custom layout.
# •	Window icon and title updated via .iconbitmap() and .title().

import tkinter as tk
from tkinter import messagebox

def update_name():
    new_name=name_entry.get()
    if new_name:
        name_label.config(text=new_name)
    else:
        messagebox.showerror("Input Error", "Name cannot be empty!")

root=tk.Tk()
root.title("Portfolio Dashboard")
root.geometry("500x500")
root.iconbitmap("icon.ico")

name_label = tk.Label(root, text="Your Name", font=("Helvetica", 16, "bold"))
name_label.place(x=150, y=30)

name_entry = tk.Entry(root, width=25)
name_entry.place(x=120, y=70)

update_button = tk.Button(root, text="Update Name", command=update_name)
update_button.place(x=150, y=100)

email_label = tk.Label(root, text="Email:")
email_label.place(x=50, y=150)
email_entry = tk.Entry(root, width=30)
email_entry.place(x=120, y=150)

phone_label = tk.Label(root, text="Phone:")
phone_label.place(x=50, y=180)
phone_entry = tk.Entry(root, width=30)
phone_entry.place(x=120, y=180)

bio_label = tk.Label(root, text="Bio:")
bio_label.place(x=50, y=220)
bio_text = tk.Text(root, width=30, height=5)
bio_text.place(x=120, y=220)

root.mainloop()

