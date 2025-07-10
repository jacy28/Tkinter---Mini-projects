# 🔰 12. Contact CSV Importer (SQLite + FileDialog)
# Goal: Import contact details from a .csv file into SQLite.
# Requirements:
# •	Use askopenfilename() to load file.
# •	Read line by line and insert into DB.
# •	Validate data.
# •	Show success message in Label.

import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import csv
import re

conn = sqlite3.connect("contacts.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT
    )
""")
conn.commit()

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_phone(phone):
    return phone.isdigit() and 7 <= len(phone) <= 15

def import_csv():
    file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file:
        return

    success_count = 0
    error_count = 0

    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                error_count += 1
                continue
            name, email, phone = row
            name, email, phone = name.strip(), email.strip(), phone.strip()
            if not name or not is_valid_email(email) or not is_valid_phone(phone):
                error_count += 1
                continue
            cur.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
            success_count += 1

    conn.commit()
    status_label.config(text=f"Imported: {success_count}, Errors: {error_count}")

root = tk.Tk()
root.title("Contact CSV Importer")
root.geometry("400x200")

tk.Button(root, text="Import Contacts from CSV", command=import_csv).pack(pady=40)

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
