# ✅ 11. Product Order Form
# Scenario: GUI for selecting a product and placing an order.
# Features:
# •	Combobox for selecting product.
# •	Spinbox for quantity.
# •	Submit to add order in Listbox.
# •	Scrollbar for list.

import tkinter as tk
from tkinter import ttk

def submit_order():
    product = product_combo.get()
    quantity = quantity_spinbox.get()
    if product and quantity:
        order = f"{product} x {quantity}"
        order_listbox.insert(tk.END, order)

root = tk.Tk()
root.title("Product Order Form")
root.geometry("400x350")

tk.Label(root, text="Select Product:").pack(anchor="w", padx=10, pady=(10, 0))
product_combo = ttk.Combobox(root, values=["Laptop", "Phone", "Tablet", "Monitor"], state="readonly", width=30)
product_combo.pack(padx=10, pady=5)

tk.Label(root, text="Quantity:").pack(anchor="w", padx=10, pady=(10, 0))
quantity_spinbox = tk.Spinbox(root, from_=1, to=30, width=5)
quantity_spinbox.pack(padx=10, pady=5)

tk.Button(root, text="Submit Order", command=submit_order).pack(pady=15)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

order_listbox = tk.Listbox(root, width=50, height=10, yscrollcommand=scrollbar.set)
order_listbox.pack(padx=10, pady=10)
scrollbar.config(command=order_listbox.yview)

root.mainloop()
