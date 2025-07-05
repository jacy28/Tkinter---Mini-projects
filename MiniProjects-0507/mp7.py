# 🟢 7. Contact Book with Listbox
# Goal: Store and display contact names.
# Requirements:
# •	Entry for name and number.
# •	Button to add to Listbox.
# •	Use Scrollbar with Listbox.
# •	Bind double-click to show selected contact in Label.
# •	Clear all entries on another button.

import tkinter as tk

root = tk.Tk()
root.title("Contact Book")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Number:").grid(row=1, column=0, padx=5, pady=5, sticky="e")

name_entry = tk.Entry(root)
number_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)
number_entry.grid(row=1, column=1, padx=5, pady=5)

def add_contact():
    name = name_entry.get().strip()
    number = number_entry.get().strip()
    if name and number:
        contact_listbox.insert(tk.END, f"{name} - {number}")
        name_entry.delete(0, tk.END)
        number_entry.delete(0, tk.END)

def clear_all():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    contact_listbox.delete(0, tk.END)
    selected_var.set("")

def show_selected(event):
    selection = contact_listbox.curselection()
    if selection:
        contact = contact_listbox.get(selection[0])
        selected_var.set(f"Selected: {contact}")

add_btn = tk.Button(root, text="Add Contact", command=add_contact)
add_btn.grid(row=2, column=0, columnspan=2, pady=5)

clear_btn = tk.Button(root, text="Clear All", command=clear_all)
clear_btn.grid(row=3, column=0, columnspan=2, pady=5)

list_frame = tk.Frame(root)
list_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

contact_listbox = tk.Listbox(list_frame, width=40, height=10)
scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=contact_listbox.yview)
contact_listbox.config(yscrollcommand=scrollbar.set)

contact_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

contact_listbox.bind("<Double-Button-1>", show_selected)

selected_var = tk.StringVar()
selected_label = tk.Label(root, textvariable=selected_var)
selected_label.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
