# 🟢 18. Customer Order Form
# Goal: Input order and display in Listbox.
# Requirements:
# •	Entry for name.
# •	Combobox for product.
# •	Spinbox for quantity.
# •	Submit button adds to Listbox.
# •	Scrollbar for listbox if many orders.

import tkinter as tk
from tkinter import ttk

def submit_order():
    name = name_entry.get()
    product = product_combobox.get()
    quantity = quantity_spinbox.get()

    if not name or not product or not quantity:
        return

    order = f"{name} ordered {quantity} x {product}"
    order_listbox.insert(tk.END, order)

    name_entry.delete(0, tk.END)
    product_combobox.set('')
    quantity_spinbox.set(1)

root = tk.Tk()
root.title("Customer Order Form")
root.geometry("400x300")

form_frame = tk.Frame(root)
form_frame.grid(row=0, column=0, padx=20, pady=20)

name_label = tk.Label(form_frame, text="Customer Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1)

product_label = tk.Label(form_frame, text="Product:")
product_label.grid(row=1, column=0, sticky="w", pady=10)
product_combobox = ttk.Combobox(form_frame, values=["Laptop", "Phone", "Headphones", "Monitor"], state="readonly")
product_combobox.grid(row=1, column=1)

quantity_label = tk.Label(form_frame, text="Quantity:")
quantity_label.grid(row=2, column=0, sticky="w")
quantity_spinbox = tk.Spinbox(form_frame, from_=1, to=10, width=5)
quantity_spinbox.grid(row=2, column=1)

submit_button = tk.Button(root, text="Submit Order", command=submit_order)
submit_button.grid(row=1, column=0, pady=10)

list_frame = tk.Frame(root)
list_frame.grid(row=2, column=0, padx=20, pady=10)

scrollbar = tk.Scrollbar(list_frame, orient="vertical")
order_listbox = tk.Listbox(list_frame, width=45, height=8, yscrollcommand=scrollbar.set)
scrollbar.config(command=order_listbox.yview)

order_listbox.grid(row=0, column=0)
scrollbar.grid(row=0, column=1, sticky="ns")

root.mainloop()
