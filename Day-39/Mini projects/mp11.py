# 11.	Contact Book (Very Basic)
# 	Entries for name and phone, Button to add, Label or Text to show stored contacts.

import tkinter as tk
from tkinter import messagebox

# Function to add contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Please enter both name and phone.")
        return

    contact = f"Name: {name}, Phone: {phone}\n"
    contacts_text.insert(tk.END, contact)

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Basic Contact Book")
root.geometry("400x350")

# Name input
tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# Phone input
tk.Label(root, text="Phone:").pack(pady=5)
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()

# Add button
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=10)

# Contact display area
tk.Label(root, text="Stored Contacts:").pack(pady=5)
contacts_text = tk.Text(root, width=40, height=10)
contacts_text.pack(pady=5)

# Scrollbar
scrollbar = tk.Scrollbar(root, command=contacts_text.yview)
scrollbar.pack(side="right", fill="y")
contacts_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
