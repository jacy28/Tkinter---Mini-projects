# ✅ 18. Inventory Stock Tracker
# Scenario: Add and track items and stock count.
# Features:
# •	Entry for item name.
# •	Spinbox for quantity.
# •	Add to Listbox with current stock.
# •	Scrollbar for large stock list.

import tkinter as tk
from tkinter import messagebox

def add_item():
    item = item_entry.get().strip()
    quantity = quantity_spinbox.get()

    if not item:
        messagebox.showerror("Input Error", "Item name cannot be empty.")
        return

    entry = f"{item} - Qty: {quantity}"
    stock_listbox.insert(tk.END, entry)
    item_entry.delete(0, tk.END)
    quantity_spinbox.delete(0, tk.END)
    quantity_spinbox.insert(0, "1")

root = tk.Tk()
root.title("Inventory Stock Tracker")
root.geometry("400x350")

tk.Label(root, text="Item Name:").pack(anchor="w", padx=10, pady=(10, 0))
item_entry = tk.Entry(root)
item_entry.pack(padx=10, fill="x")

tk.Label(root, text="Quantity:").pack(anchor="w", padx=10, pady=(10, 0))
quantity_spinbox = tk.Spinbox(root, from_=1, to=999)
quantity_spinbox.pack(padx=10, fill="x")

tk.Button(root, text="Add to Stock", command=add_item).pack(pady=10)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

stock_listbox = tk.Listbox(frame)
stock_listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame, command=stock_listbox.yview)
scrollbar.pack(side="right", fill="y")
stock_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
