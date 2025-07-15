# 🔷 5. Grocery Order Interface
# Widgets Used: Listbox, Combobox, Spinbox, Scrollbar
# Requirements:
# •	Combobox to choose product category (Fruits, Vegetables, Drinks).
# •	Listbox to show products based on category.
# •	Spinbox to select quantity.
# •	Button to "Add to Cart" and another Listbox to show the order.
# •	Scrollbar for large list of products or cart items.

import tkinter as tk
from tkinter import ttk

# Sample product data
products = {
    "Fruits": ["Apple", "Banana", "Mango", "Grapes", "Orange", "Pineapple", "Watermelon"],
    "Vegetables": ["Tomato", "Carrot", "Potato", "Onion", "Spinach", "Cabbage", "Cucumber"],
    "Drinks": ["Water", "Juice", "Soda", "Tea", "Coffee", "Milk", "Smoothie"]
}

def update_product_list(event=None):
    """Update products based on selected category"""
    category = category_combo.get()
    product_listbox.delete(0, tk.END)
    for item in products.get(category, []):
        product_listbox.insert(tk.END, item)

def add_to_cart():
    selected = product_listbox.curselection()
    if not selected:
        return
    item = product_listbox.get(selected[0])
    quantity = qty_spinbox.get()
    cart_listbox.insert(tk.END, f"{item} x {quantity}")

# --- GUI Setup ---
root = tk.Tk()
root.title("🔷 Grocery Order Interface")
root.geometry("600x400")

# --- Category Selection ---
tk.Label(root, text="Category:").pack()
category_combo = ttk.Combobox(root, values=list(products.keys()), state="readonly", width=20)
category_combo.set("Fruits")
category_combo.pack(pady=5)
category_combo.bind("<<ComboboxSelected>>", update_product_list)

# --- Product Listbox + Scrollbar ---
product_frame = tk.Frame(root)
product_frame.pack(pady=10)

product_scroll = tk.Scrollbar(product_frame)
product_scroll.pack(side=tk.RIGHT, fill=tk.Y)

product_listbox = tk.Listbox(product_frame, height=8, width=30, yscrollcommand=product_scroll.set)
product_listbox.pack(side=tk.LEFT)
product_scroll.config(command=product_listbox.yview)

update_product_list()  # Initialize with Fruits

# --- Quantity Spinbox ---
tk.Label(root, text="Quantity:").pack(pady=(10, 0))
qty_spinbox = tk.Spinbox(root, from_=1, to=50, width=5)
qty_spinbox.pack()

# --- Add to Cart Button ---
tk.Button(root, text="Add to Cart", command=add_to_cart).pack(pady=10)

# --- Cart Listbox + Scrollbar ---
cart_label = tk.Label(root, text="🛒 Cart:")
cart_label.pack()

cart_frame = tk.Frame(root)
cart_frame.pack(pady=5)

cart_scroll = tk.Scrollbar(cart_frame)
cart_scroll.pack(side=tk.RIGHT, fill=tk.Y)

cart_listbox = tk.Listbox(cart_frame, height=8, width=40, yscrollcommand=cart_scroll.set)
cart_listbox.pack(side=tk.LEFT)
cart_scroll.config(command=cart_listbox.yview)

root.mainloop()
