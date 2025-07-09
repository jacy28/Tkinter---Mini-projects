# ✅ 6. Contact Book App
# Objective: Store, view, and edit contacts.
# Requirements:
# •	Use PanedWindow for layout (left: list, right: form).
# •	Toolbar with "Add", "Edit", "Delete" buttons.
# •	Menu bar for File > Export, Exit.
# •	Use dialogs to confirm deletion or export.

import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def refresh_listbox():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, contact["name"])

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    phone = simpledialog.askstring("Add Contact", "Enter phone:")
    if name and phone:
        contacts.append({"name": name, "phone": phone})
        refresh_listbox()

def edit_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select", "No contact selected.")
        return
    index = selected[0]
    contact = contacts[index]
    name = simpledialog.askstring("Edit Contact", "Edit name:", initialvalue=contact["name"])
    phone = simpledialog.askstring("Edit Contact", "Edit phone:", initialvalue=contact["phone"])
    if name and phone:
        contacts[index] = {"name": name, "phone": phone}
        refresh_listbox()
        show_contact(index)

def delete_contact():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select", "No contact selected.")
        return
    index = selected[0]
    confirm = messagebox.askyesno("Delete", "Are you sure you want to delete this contact?")
    if confirm:
        contacts.pop(index)
        refresh_listbox()
        clear_form()

def export_contacts():
    confirm = messagebox.askokcancel("Export", "Export contacts to file?")
    if confirm:
        print("Contacts exported.")  # Replace with file write logic
        messagebox.showinfo("Exported", "Contacts exported successfully.")

def show_contact(index):
    contact = contacts[index]
    name_var.set(contact["name"])
    phone_var.set(contact["phone"])

def on_select(event):
    selected = listbox.curselection()
    if selected:
        show_contact(selected[0])

def clear_form():
    name_var.set("")
    phone_var.set("")

root = tk.Tk()
root.title("Contact Book")
root.geometry("600x400")

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Export", command=export_contacts)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)

toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="Add", command=add_contact).pack(side="left", padx=2)
tk.Button(toolbar, text="Edit", command=edit_contact).pack(side="left", padx=2)
tk.Button(toolbar, text="Delete", command=delete_contact).pack(side="left", padx=2)

pane = tk.PanedWindow(root, sashrelief="raised", sashwidth=5)
pane.pack(fill="both", expand=True)

left_frame = tk.Frame(pane)
listbox = tk.Listbox(left_frame)
listbox.pack(fill="both", expand=True, padx=5, pady=5)
listbox.bind("<<ListboxSelect>>", on_select)
pane.add(left_frame)

right_frame = tk.Frame(pane, padx=10, pady=10)
name_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(right_frame, text="Name:").grid(row=0, column=0, sticky="e")
tk.Entry(right_frame, textvariable=name_var).grid(row=0, column=1)

tk.Label(right_frame, text="Phone:").grid(row=1, column=0, sticky="e")
tk.Entry(right_frame, textvariable=phone_var).grid(row=1, column=1)

pane.add(right_frame)

root.mainloop()
