# 12. Scrollable Product List
# Objective: Display and manage a long product list.
# Features:
# •	Listbox populated with 50+ items.
# •	Scrollbar for vertical navigation.
# •	Click item to show details in Label.
# •	Use Frame to group widgets.
# •	Buttons to delete or add products.

import tkinter as tk
from tkinter import simpledialog, messagebox

def show_details(event):
    selected = product_listbox.curselection()
    if selected:
        item = product_listbox.get(selected)
        details_label.config(text=f"Selected Product:\n{item}")

def add_product():
    new_item = simpledialog.askstring("Add Product", "Enter product name:")
    if new_item:
        product_listbox.insert(tk.END, new_item)

def delete_product():
    selected = product_listbox.curselection()
    if selected:
        product_listbox.delete(selected)
        details_label.config(text="Product deleted.")
    else:
        messagebox.showwarning("Delete", "No product selected.")

root = tk.Tk()
root.title("Scrollable Product List")
root.geometry("400x400")

list_frame = tk.Frame(root)
list_frame.pack(pady=10)

product_listbox = tk.Listbox(list_frame, width=40, height=15)
scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=product_listbox.yview)
product_listbox.config(yscrollcommand=scrollbar.set)

product_listbox.pack(side="left", fill="y")
scrollbar.pack(side="right", fill="y")

for i in range(1, 61):
    product_listbox.insert(tk.END, f"Product #{i}")

product_listbox.bind("<<ListboxSelect>>", show_details)

action_frame = tk.Frame(root)
action_frame.pack(pady=10)

details_label = tk.Label(action_frame, text="Select a product to see details.", wraplength=300, justify="left")
details_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add Product", command=add_product)
add_btn.pack(side="left", padx=10)

delete_btn = tk.Button(button_frame, text="Delete Selected", command=delete_product)
delete_btn.pack(side="left", padx=10)

root.mainloop()
