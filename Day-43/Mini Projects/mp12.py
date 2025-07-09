# ✅ 12. Database Viewer GUI
# Objective: Load and display database records.
# Requirements:
# •	Use PanedWindow to split filter/search on top and results below.
# •	Add Menu: Data > Load DB, Exit.
# •	Add Toolbar: Refresh, Filter.
# •	Show messagebox.showinfo() on DB load success.

import tkinter as tk
from tkinter import ttk, messagebox

# Simulated data
sample_data = [
    {"ID": 1, "Name": "Alice", "Email": "alice@example.com"},
    {"ID": 2, "Name": "Bob", "Email": "bob@example.com"},
    {"ID": 3, "Name": "Charlie", "Email": "charlie@example.com"}
]

def load_database():
    for row in tree.get_children():
        tree.delete(row)
    for record in sample_data:
        tree.insert("", "end", values=(record["ID"], record["Name"], record["Email"]))
    messagebox.showinfo("Database", "Database loaded successfully.")

def refresh_data():
    load_database()

def filter_data():
    query = search_entry.get().lower()
    for row in tree.get_children():
        tree.delete(row)
    for record in sample_data:
        if query in record["Name"].lower() or query in record["Email"].lower():
            tree.insert("", "end", values=(record["ID"], record["Name"], record["Email"]))

root = tk.Tk()
root.title("Database Viewer")
root.geometry("500x400")

# Menu
menubar = tk.Menu(root)
data_menu = tk.Menu(menubar, tearoff=0)
data_menu.add_command(label="Load DB", command=load_database)
data_menu.add_separator()
data_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Data", menu=data_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root, bg="#eee")
toolbar.pack(fill="x")
tk.Button(toolbar, text="Refresh", command=refresh_data).pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Filter", command=filter_data).pack(side="left", padx=5, pady=5)

# PanedWindow
paned = tk.PanedWindow(root, orient=tk.VERTICAL)
paned.pack(fill="both", expand=True)

# Top frame (filter input)
top_frame = tk.Frame(paned)
tk.Label(top_frame, text="Search:").pack(side="left", padx=5, pady=5)
search_entry = tk.Entry(top_frame)
search_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
paned.add(top_frame, height=40)

# Bottom frame (table display)
bottom_frame = tk.Frame(paned)
tree = ttk.Treeview(bottom_frame, columns=("ID", "Name", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.pack(fill="both", expand=True, padx=10, pady=10)
paned.add(bottom_frame)

root.mainloop()
