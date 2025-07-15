# 🛒 3. Basic Product Order Form
# Goal: A form where users select products, input quantity, and place an order.
# Requirements:
# •	Use Entry for quantity input.
# •	Use Label for product names and prices.
# •	Show total price dynamically.
# •	Validate numeric input.
# •	Use grid() for form layout.

import tkinter as tk

root = tk.Tk()
root.title("🛒 Product Order Form")
root.geometry("400x300")

# --- Products List (Name, Price) ---
products = [
    ("Apple", 350),
    ("Banana", 120),
    ("Orange", 280),
    ("Grapes", 300)
]

entries = []
quantity_vars = []

# --- Function to validate numeric input and update total ---
def update_total(*args):
    total = 0
    for idx, var in enumerate(quantity_vars):
        qty_str = var.get()
        if qty_str.isdigit():
            qty = int(qty_str)
            total += qty * products[idx][1]
        elif qty_str != "":
            total_label.config(text="Enter numbers only!", fg="red")
            return
    total_label.config(text=f"Total: ${total:.2f}", fg="green")

# --- UI Layout ---
tk.Label(root, text="Product", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Price", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10)
tk.Label(root, text="Quantity", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10)

# Product rows
for i, (name, price) in enumerate(products, start=1):
    tk.Label(root, text=name).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    tk.Label(root, text=f"${price:.2f}").grid(row=i, column=1, padx=10)

    var = tk.StringVar()
    var.trace_add("write", update_total)
    quantity_vars.append(var)

    entry = tk.Entry(root, textvariable=var, width=5)
    entry.grid(row=i, column=2, padx=10)
    entries.append(entry)

# Total Price Label
total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"), fg="green")
total_label.grid(row=len(products)+1, column=0, columnspan=3, pady=20)

root.mainloop()
