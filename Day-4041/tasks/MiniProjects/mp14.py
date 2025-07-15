# 📦 14. Inventory Input Form
# Goal: Form to input item name, quantity, price and calculate total.
# Requirements:
# •	Fields: Item, Qty, Price.
# •	Compute total price.
# •	Display all items in Text widget.
# •	Use grid() layout.

import tkinter as tk

# --- Function to add item to inventory ---
def add_item():
    item = item_entry.get()
    qty = qty_entry.get()
    price = price_entry.get()

    # Validate input
    if not item or not qty or not price:
        message_label.config(text="❗ All fields required", fg="red")
        return
    if not qty.isdigit() or not price.replace('.', '', 1).isdigit():
        message_label.config(text="❗ Quantity & Price must be numeric", fg="red")
        return

    qty = int(qty)
    price = float(price)
    total = qty * price

    # Add to display
    output.insert(tk.END, f"{item:<15} Qty: {qty:<3} Price: ${price:.2f} → Total: ${total:.2f}\n")
    
    # Clear entries and message
    item_entry.delete(0, tk.END)
    qty_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    message_label.config(text="✅ Item added!", fg="green")

# --- GUI Setup ---
root = tk.Tk()
root.title("📦 Inventory Input Form")
root.geometry("500x400")

# --- Labels and Entries ---
tk.Label(root, text="Item Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
item_entry = tk.Entry(root)
item_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Quantity:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
qty_entry = tk.Entry(root)
qty_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Price:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=5)

# --- Add Button ---
add_btn = tk.Button(root, text="Add Item", command=add_item)
add_btn.grid(row=3, column=1, pady=10)

# --- Message Label ---
message_label = tk.Label(root, text="", font=("Arial", 10))
message_label.grid(row=4, column=0, columnspan=2)

# --- Output Text Widget ---
output = tk.Text(root, height=10, width=55)
output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Optional: header line
output.insert(tk.END, "Inventory List:\n")
output.insert(tk.END, "-" * 50 + "\n")

root.mainloop()
