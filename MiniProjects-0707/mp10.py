# ✅ 10. Contact Book Manager
# Scenario: Maintain a list of contact entries.
# Features:
# •	Entry for name, phone.
# •	Add contacts to Listbox.
# •	Scrollbar for large list.
# •	Buttons for Add, Delete, Clear All.

import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    if name and phone:
        contact_listbox.insert(tk.END, f"{name} - {phone}")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Input Error", "Both name and phone are required.")

def delete_contact():
    selected = contact_listbox.curselection()
    for i in reversed(selected):
        contact_listbox.delete(i)

def clear_contacts():
    contact_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Book Manager")
root.geometry("400x400")

tk.Label(root, text="Name:").pack(anchor="w", padx=10, pady=(10, 0))
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=10)

tk.Label(root, text="Phone:").pack(anchor="w", padx=10, pady=(10, 0))
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", command=add_contact).pack(side="left", padx=5)
tk.Button(btn_frame, text="Delete", command=delete_contact).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear All", command=clear_contacts).pack(side="left", padx=5)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

contact_listbox = tk.Listbox(root, width=50, height=15, yscrollcommand=scrollbar.set)
contact_listbox.pack(padx=10, pady=10)
scrollbar.config(command=contact_listbox.yview)

root.mainloop()
