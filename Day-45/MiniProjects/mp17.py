# 🔰 17. Book Library Manager (SQLite + Form)
# Goal: Add/manage books with author, title, year.
# Requirements:
# •	SQLite-backed form.
# •	Display books in Listbox.
# •	Edit and delete options.
# •	Confirmation dialog before delete.

import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER
    )
""")
conn.commit()

def refresh_list():
    listbox.delete(0, tk.END)
    for row in cur.execute("SELECT * FROM books"):
        listbox.insert(tk.END, row)

def add_book():
    title = title_var.get().strip()
    author = author_var.get().strip()
    year = year_var.get().strip()
    if not title or not author or not year.isdigit():
        return
    cur.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, int(year)))
    conn.commit()
    title_var.set("")
    author_var.set("")
    year_var.set("")
    refresh_list()

def delete_book():
    selected = listbox.curselection()
    if not selected:
        return
    item = listbox.get(selected)
    confirm = messagebox.askyesno("Confirm Delete", f"Delete '{item[1]}'?")
    if confirm:
        cur.execute("DELETE FROM books WHERE id=?", (item[0],))
        conn.commit()
        refresh_list()

def edit_book():
    selected = listbox.curselection()
    if not selected:
        return
    item = listbox.get(selected)
    title_var.set(item[1])
    author_var.set(item[2])
    year_var.set(str(item[3]))
    cur.execute("DELETE FROM books WHERE id=?", (item[0],))
    conn.commit()
    refresh_list()

root = tk.Tk()
root.title("Book Library Manager")
root.geometry("500x400")

title_var = tk.StringVar()
author_var = tk.StringVar()
year_var = tk.StringVar()

tk.Label(root, text="Title").pack()
tk.Entry(root, textvariable=title_var).pack(fill="x", padx=10)

tk.Label(root, text="Author").pack()
tk.Entry(root, textvariable=author_var).pack(fill="x", padx=10)

tk.Label(root, text="Year").pack()
tk.Entry(root, textvariable=year_var).pack(fill="x", padx=10)

tk.Button(root, text="Add Book", command=add_book).pack(pady=5)
tk.Button(root, text="Edit Selected", command=edit_book).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_book).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(fill="both", expand=True, padx=10, pady=10)

refresh_list()
root.mainloop()
