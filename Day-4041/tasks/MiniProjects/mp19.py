# 📊 19. Expense Tracker
# Goal: Log and total daily expenses.
# Requirements:
# •	Input: Item name and amount.
# •	Show itemized list in Text.
# •	Show total below.
# •	Use grid() for form, pack() for summary.

import tkinter as tk

# --- Main Window ---
root = tk.Tk()
root.title("📊 Expense Tracker")
root.geometry("400x400")

# --- Global Variables ---
total_expense = 0.0

# --- Functions ---
def add_expense():
    global total_expense

    item = item_entry.get().strip()
    amount = amount_entry.get().strip()

    if not item or not amount:
        message_label.config(text="Both fields are required.", fg="red")
        return

    try:
        amount_val = float(amount)
        total_expense += amount_val
        expense_display.insert(tk.END, f"{item}: ${amount_val:.2f}\n")
        total_label.config(text=f"Total: ${total_expense:.2f}", fg="green")
        message_label.config(text="Added successfully!", fg="blue")

        # Clear inputs
        item_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

    except ValueError:
        message_label.config(text="Enter a valid number for amount.", fg="red")

# --- Layout (grid for form) ---
tk.Label(root, text="Item Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
item_entry = tk.Entry(root, width=25)
item_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
amount_entry = tk.Entry(root, width=25)
amount_entry.grid(row=1, column=1, padx=10, pady=5)

add_btn = tk.Button(root, text="Add Expense", command=add_expense)
add_btn.grid(row=2, column=1, pady=10)

message_label = tk.Label(root, text="", fg="red")
message_label.grid(row=3, column=0, columnspan=2)

# --- Summary (pack for display) ---
expense_display = tk.Text(root, height=10, width=45)
expense_display.grid(row=4, column=0, columnspan=2, pady=10)

total_label = tk.Label(root, text="Total: $0.00", font=("Arial", 12, "bold"), fg="green")
total_label.grid(row=5, column=0, columnspan=2)

# --- Start ---
root.mainloop()
