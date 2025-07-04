# 17. Customer Drop-down Selector
# Objective: Choose customer and view info.
# Features:
# •	Use Combobox to select customer.
# •	Display details (name, contact, address) in Labels.
# •	Change details dynamically based on selection.
# •	Disable ComboBox after selection if needed.

import tkinter as tk
from tkinter import ttk

def show_customer_info(event=None):
    selected = customer_combo.get()
    info = customers.get(selected)
    if info:
        name_label.config(text=f"Name: {info['name']}")
        contact_label.config(text=f"Contact: {info['contact']}")
        address_label.config(text=f"Address: {info['address']}")
        if disable_after_selection.get():
            customer_combo.config(state="disabled")

def reset_selection():
    customer_combo.config(state="readonly")
    customer_combo.set("")
    name_label.config(text="Name:")
    contact_label.config(text="Contact:")
    address_label.config(text="Address:")

customers = {
    "C001": {"name": "Alice Smith", "contact": "555-1234", "address": "123 Apple St"},
    "C002": {"name": "Bob Johnson", "contact": "555-5678", "address": "456 Berry Ave"},
    "C003": {"name": "Charlie Lee", "contact": "555-9876", "address": "789 Cherry Blvd"},
}

root = tk.Tk()
root.title("Customer Selector")
root.geometry("400x300")

tk.Label(root, text="Select Customer ID:").pack(pady=10)
customer_combo = ttk.Combobox(root, values=list(customers.keys()), state="readonly")
customer_combo.pack()
customer_combo.bind("<<ComboboxSelected>>", show_customer_info)

disable_after_selection = tk.BooleanVar()
disable_check = tk.Checkbutton(root, text="Disable after selection", variable=disable_after_selection)
disable_check.pack(pady=5)

info_frame = tk.Frame(root)
info_frame.pack(pady=20)

name_label = tk.Label(info_frame, text="Name:", anchor="w", width=40)
name_label.pack(anchor="w")
contact_label = tk.Label(info_frame, text="Contact:", anchor="w", width=40)
contact_label.pack(anchor="w")
address_label = tk.Label(info_frame, text="Address:", anchor="w", width=40)
address_label.pack(anchor="w")

tk.Button(root, text="Reset", command=reset_selection).pack(pady=10)

root.mainloop()
