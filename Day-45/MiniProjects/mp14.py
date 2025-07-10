# 🔰 14. Expense Tracker App (File Save + SQLite)
# Goal: Manage expenses with category and amount.
# Requirements:
# •	Add/Edit/Delete entries.
# •	Store in SQLite.
# •	Export report as .txt via asksaveasfilename().
# •	Add total and category filter.

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT,
        amount REAL
    )
""")
conn.commit()

def add_entry():
    cat = category_var.get().strip()
    amt = amount_var.get().strip()
    if not cat or not amt.replace('.', '', 1).isdigit():
        return
    cur.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (cat, float(amt)))
    conn.commit()
    category_var.set("")
    amount_var.set("")
    load_data()

def delete_entry():
    selected = tree.selection()
    if selected:
        item_id = tree.item(selected)["values"][0]
        cur.execute("DELETE FROM expenses WHERE id=?", (item_id,))
        conn.commit()
        load_data()

def edit_entry():
    selected = tree.selection()
    if selected:
        item = tree.item(selected)["values"]
        category_var.set(item[1])
        amount_var.set(str(item[2]))
        cur.execute("DELETE FROM expenses WHERE id=?", (item[0],))
        conn.commit()
        load_data()

def load_data(filter_cat=""):
    for i in tree.get_children():
        tree.delete(i)
    if filter_cat:
        rows = cur.execute("SELECT * FROM expenses WHERE category=?", (filter_cat,))
    else:
        rows = cur.execute("SELECT * FROM expenses")
    total = 0
    for row in rows:
        tree.insert("", "end", values=row)
        total += row[2]
    total_label.config(text=f"Total: ₹{total:.2f}")

def export_report():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not file:
        return
    rows = cur.execute("SELECT * FROM expenses").fetchall()
    with open(file, "w") as f:
        total = 0
        for row in rows:
            f.write(f"{row[1]} - ₹{row[2]:.2f}\n")
            total += row[2]
        f.write(f"\nTotal: ₹{total:.2f}")
    messagebox.showinfo("Exported", "Report exported successfully.")

def filter_by_category():
    cat = filter_var.get().strip()
    load_data(cat)

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x500")

category_var = tk.StringVar()
amount_var = tk.StringVar()
filter_var = tk.StringVar()

tk.Label(root, text="Category").pack()
tk.Entry(root, textvariable=category_var).pack(fill="x", padx=10)

tk.Label(root, text="Amount").pack()
tk.Entry(root, textvariable=amount_var).pack(fill="x", padx=10)

tk.Button(root, text="Add", command=add_entry).pack(pady=5)
tk.Button(root, text="Edit Selected", command=edit_entry).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_entry).pack(pady=5)

columns = ("ID", "Category", "Amount")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True, pady=10)

total_label = tk.Label(root, text="Total: ₹0.00")
total_label.pack()

tk.Label(root, text="Filter by Category").pack()
tk.Entry(root, textvariable=filter_var).pack(fill="x", padx=10)
tk.Button(root, text="Apply Filter", command=filter_by_category).pack(pady=5)

tk.Button(root, text="Export Report", command=export_report).pack(pady=10)

load_data()
root.mainloop()
