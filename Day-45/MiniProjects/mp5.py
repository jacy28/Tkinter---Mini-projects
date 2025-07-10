# 🔰 5. SQLite Address Book
# Goal: CRUD app to manage contacts.
# Requirements:
# •	Fields: Name, Email, Phone.
# •	Add/Edit/Delete/Search contacts using SQLite.
# •	Confirmation dialog on delete.
# •	Store search result in Listbox.

import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("address_book.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT,
        phone TEXT
    )
""")
conn.commit()

def refresh_listbox(results=None):
    listbox.delete(0, tk.END)
    data = results if results else cur.execute("SELECT * FROM contacts").fetchall()
    for row in data:
        listbox.insert(tk.END, f"{row[0]} - {row[1]} | {row[2]} | {row[3]}")

def add_contact():
    name, email, phone = name_var.get(), email_var.get(), phone_var.get()
    if not name:
        messagebox.showwarning("Required", "Name is required.")
        return
    cur.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    refresh_listbox()
    clear_fields()

def edit_contact():
    selection = listbox.curselection()
    if not selection:
        return
    contact_id = int(listbox.get(selection[0]).split(" - ")[0])
    name, email, phone = name_var.get(), email_var.get(), phone_var.get()
    if not name:
        messagebox.showwarning("Required", "Name is required.")
        return
    cur.execute("UPDATE contacts SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, contact_id))
    conn.commit()
    refresh_listbox()
    clear_fields()

def delete_contact():
    selection = listbox.curselection()
    if not selection:
        return
    contact_id = int(listbox.get(selection[0]).split(" - ")[0])
    if messagebox.askyesno("Confirm", "Delete this contact?"):
        cur.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        refresh_listbox()
        clear_fields()

def search_contacts():
    keyword = search_var.get()
    results = cur.execute("SELECT * FROM contacts WHERE name LIKE ?", (f"%{keyword}%",)).fetchall()
    refresh_listbox(results)

def load_selected(event):
    selection = listbox.curselection()
    if not selection:
        return
    contact = listbox.get(selection[0])
    contact_id = int(contact.split(" - ")[0])
    cur.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
    row = cur.fetchone()
    name_var.set(row[1])
    email_var.set(row[2])
    phone_var.set(row[3])

def clear_fields():
    name_var.set("")
    email_var.set("")
    phone_var.set("")

root = tk.Tk()
root.title("SQLite Address Book")
root.geometry("500x500")

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
search_var = tk.StringVar()

tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Email").pack()
tk.Entry(root, textvariable=email_var).pack()

tk.Label(root, text="Phone").pack()
tk.Entry(root, textvariable=phone_var).pack()

tk.Button(root, text="Add", command=add_contact).pack(pady=2)
tk.Button(root, text="Edit", command=edit_contact).pack(pady=2)
tk.Button(root, text="Delete", command=delete_contact).pack(pady=2)

tk.Label(root, text="Search by Name").pack(pady=(10, 0))
tk.Entry(root, textvariable=search_var).pack()
tk.Button(root, text="Search", command=search_contacts).pack(pady=2)

listbox = tk.Listbox(root, width=60)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", load_selected)

refresh_listbox()
root.mainloop()
