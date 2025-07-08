# 12.	Simple Address Form
# 	Form with Entries for name, address, phone, etc., and a Button to display the filled information.

import tkinter as tk
from tkinter import messagebox

# Function to show filled info
def display_info():
    name = name_entry.get().strip()
    address = address_entry.get("1.0", tk.END).strip()
    phone = phone_entry.get().strip()

    if not name or not address or not phone:
        messagebox.showerror("Missing Fields", "Please fill out all fields.")
        return

    info = f"Name: {name}\nPhone: {phone}\nAddress:\n{address}"
    messagebox.showinfo("Submitted Info", info)

# GUI setup
root = tk.Tk()
root.title("Address Form")
root.geometry("400x350")

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Phone
tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

# Address
tk.Label(root, text="Address:").grid(row=2, column=0, padx=10, pady=5, sticky="ne")
address_entry = tk.Text(root, width=30, height=4)
address_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=display_info)
submit_btn.grid(row=3, column=1, padx=10, pady=20, sticky="e")

root.mainloop()
