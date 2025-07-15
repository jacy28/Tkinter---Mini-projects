# 🔷 12. Customer Feedback Collector
# Widgets Used: Entry, Listbox, Scrollbar, Combobox
# Requirements:
# •	Combobox to choose feedback category (Service, Product, Delivery).
# •	Entry for name and message.
# •	Submit button to add to Listbox.
# •	Scrollbar for large feedback list.
# •	Filter feedback by category.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("🔷 Customer Feedback Collector")
root.geometry("500x400")

feedback_data = []

# --- Submit Feedback ---
def submit_feedback():
    name = name_entry.get().strip()
    message = message_entry.get().strip()
    category = category_combo.get()

    if not name or not message or not category:
        return

    entry = f"[{category}] {name}: {message}"
    feedback_data.append((category, entry))
    update_listbox()
    name_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)

# --- Update Listbox Based on Filter ---
def update_listbox():
    listbox.delete(0, tk.END)
    selected_filter = filter_combo.get()
    for cat, entry in feedback_data:
        if selected_filter == "All" or cat == selected_filter:
            listbox.insert(tk.END, entry)

# --- UI Layout ---

# Input Section
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=5, sticky="e")
name_entry = tk.Entry(input_frame, width=25)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Message:").grid(row=1, column=0, padx=5, sticky="e")
message_entry = tk.Entry(input_frame, width=25)
message_entry.grid(row=1, column=1, padx=5)

tk.Label(input_frame, text="Category:").grid(row=2, column=0, padx=5, sticky="e")
category_combo = ttk.Combobox(input_frame, values=["Service", "Product", "Delivery"], state="readonly", width=22)
category_combo.set("Service")
category_combo.grid(row=2, column=1, padx=5)

tk.Button(input_frame, text="Submit Feedback", command=submit_feedback).grid(row=3, column=0, columnspan=2, pady=10)

# Filter Section
filter_frame = tk.Frame(root)
filter_frame.pack()

tk.Label(filter_frame, text="Filter by Category:").pack(side=tk.LEFT, padx=5)
filter_combo = ttk.Combobox(filter_frame, values=["All", "Service", "Product", "Delivery"], state="readonly", width=15)
filter_combo.set("All")
filter_combo.pack(side=tk.LEFT)
filter_combo.bind("<<ComboboxSelected>>", lambda e: update_listbox())

# Feedback Display with Scrollbar
display_frame = tk.Frame(root)
display_frame.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(display_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(display_frame, yscrollcommand=scrollbar.set, height=10, width=60)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Run the App
root.mainloop()
